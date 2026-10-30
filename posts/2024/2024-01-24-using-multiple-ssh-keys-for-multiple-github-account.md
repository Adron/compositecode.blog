---
title: Using Multiple SSH Keys for Multiple Github Account
date: 2024-01-24 10:00:00 -0800
last_modified_at: 2024-01-23 13:37:50 -0800
permalink: /2024/01/24/using-multiple-ssh-keys-for-multiple-github-account/
slug: using-multiple-ssh-keys-for-multiple-github-account
wp_id: 67527
original_url: https://compositecode.blog/2024/01/24/using-multiple-ssh-keys-for-multiple-github-account/
categories:
- Unknown Code Ramblings
tags:
- git
- github
- keygen
- multiple accounts
- ssh
excerpt: 'FIRST – Setup the Keys If there is already a key, I can use this one to start with, but if there is no key to start with I’ll need to generate one. I can do this with the following command: When generating the keys, best to go with the default location, which is ~/.ssh/id_rsa. …'
image: /wp-content/uploads/2024/01/Code-1.png
---

## FIRST – Setup the Keys

If there is already a key, I can use this one to start with, but if there is no key to start with I’ll need to generate one. I can do this with the following command:

```
ssh-keygen -t rsa
```

When generating the keys, best to go with the default location, which is ~/.ssh/id\_rsa. This will create two files, id\_rsa and id\_rsa.pub. The id\_rsa file is the private key, and the id\_rsa.pub file is the public key. The private key should be kept secret, and the public key can be shared with anyone.

For the next account, which I’ll just call the work account, I’ll generate another new key. This time I’ll hand off the following parameters to the key generation to provide the work account email and the file name:

```
ssh-keygen -t rsa -C "adron.account@work_mail.com" -f "work_account_one"
```

I’ve now got two keys, one for my personal account and one for my work account.

~/.ssh/id\_rsa

~/.ssh/work\_account\_one

I’ll need to add these to the ssh-agent and the respect Github (or git whatever servers) so that I can use them.

## SECOND – Add the Keys to Github

Adding the keys to Github. We’ll start with the personal account and then add the work account. Copy the public key using `pbcopy < ~/.ssh/id_rsa.pub`. With that copied log into the Github account that this key should be associated with.

```
1. Got to *settings*.
2. Select *SSH and GPG keys* from the account user menu.
3. Navigate into `New SSH Key`, give it a title, and paste the key into the key field.
4. Click *Add SSH Key*.
```

Now log out of that Github account and into the other account, the work account. Repeat the steps above, but this time use the work account email and the work account key.

## THIRD

Register the new keys with ssh-agent. Start by checking that the ssh-agent is running with `eval "$(ssh-agent -s)"`. In the past we would add the keys to the agent with `ssh-add -K ~/.ssh/id_rsa` and `ssh-add -K ~/.ssh/work_account_one`. Now the keys are registered with the agent with the following.

```
ssh-add --apple-use-keychain ~/.ssh/id_rsa
ssh-add --apple-use-keychain ~/.ssh/work_account_one
```

## FOURTH

There is one last step, I need to tell the ssh client which key to use for which account. I can do this by adding the following to the ~/.ssh/config file.

```
# Account 1 - Primary
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
  AddKeysToAgent yes
  UseKeychain yes

# Account 2 - Second Account
Host github.com-work_user_account_name
  HostName github.com
  User git
  IdentityFile ~/.ssh/work_account_one
  AddKeysToAgent yes
  UseKeychain yes
```

Note that `work_user_account_name` is the name of the work account, not the email address. I can now use the following commands to clone repositories from the respective accounts. This tells ssh-agent to use the id\_rsa key for Git URLs starting with github.com and the work\_account\_one key for Git URLs starting with github-work\_user\_account\_name.

## FIFTH

One active SSH key per working session.

This is a good practice to follow. I can use the following command to start the ssh-agent and add the key to it.

`eval "$(ssh-agent -s)`
`ssh-add -K ~/.ssh/id_rsa`
`ssh-add ~/.ssh/id_rsa`

The same can then be done when the other key needs to be used.
