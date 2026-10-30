---
title: 'Development Workspace with Terraform on Azure: Part 1 – Install and Setup Terraform and Azure CLI'
date: 2019-08-01 15:26:18 -0700
last_modified_at: 2021-02-26 14:57:48 -0800
permalink: /2019/08/01/development-workspace-with-terraform/
slug: development-workspace-with-terraform
wp_id: 16107
original_url: https://compositecode.blog/2019/08/01/development-workspace-with-terraform/
categories:
- Azure
- How-to
- Infrastructure
tags:
- azure
- azure cli
- cli
- cloud
- cloud infrastructure
- infrastructure
- infrastructure as code
- IoC
- microsoft
- terraform
excerpt: Prerequisites before all of this. Have a basic understanding of how to use Terraform and what it does. This is covered pretty well in the Hashicorp Docs here (single page read <5 minutes) and if you have a LinkedIn Learning account check out my Terraform course “Learning Terraform“. Beyond that some basic CLI/terminal knowledge, understand where environment variables …
image: /wp-content/uploads/2019/08/terraform-azure.png
---

*Prerequisites before all of this.*

Have a basic understanding of how to use Terraform and what it does. This is covered pretty well in the Hashicorp Docs [here](https://www.terraform.io/intro/index.html) (single page read <5 minutes) and if you have a [LinkedIn Learning](https://www.linkedin.com/learning/) account check out my Terraform course “[Learning Terraform](https://www.linkedin.com/learning/learning-terraform/)“.

Beyond that some basic CLI/terminal knowledge, understand where environment variables (as I detail [here](/2018/11/06/bash-a-k-a-the-solution-for-everything-a-few-of-the-special-files/), [here](/2018/10/09/bourne-shell-as-per-v7-unix-to-todays-bash-a-k-a-the-solution-for-everything/), and [here](/2019/01/02/bash-a-k-a-the-solution-for-everything-passed-variables-the-script-filename/) for some starters) are, and miscellaneous knowledge. You’ll also need knowledge and user experience with Git. Most of these things I’ll detail explicitly but otherwise I’ll either link to or provide context for additional information throughout the article.

## 1: Terraform

**Download**

You’ll need to first install Terraform and make it available for use on your machine. To do this navigate over to the [Hashicorp](https://www.hashicorp.com/) [Terraform](https://www.terraform.io/)[Terraform](https://www.terraform.io/) site and to the [download](https://www.terraform.io/downloads.html) section. As of this time 0.12.6 is available, and for the foreseeable future this version or versions coming will be just fine.

**Install**

You’ll need to unzip this somewhere in a directory that you’ve got the path mapped for execution. In my case I’ve setup a directly I call “*Apps*” and put all of my CLI apps in that directory. Then add it to my path environment variable and then terraform becomes available to me from any terminal wherever I need it. My path variable export on Linux and Mac look like this.

```
export PATH=$PATH:/home/adron/Apps
```

Now you can verify that the Terraform CLI is available by typing `terraform` in any terminal and you should get a read out of the available Terraform commands.

For those of you who might be trying to install this on the WSL (Windows Subsystem for Linux), on Windows itself, or some variance there is specific instructions for that too. Check out [Hashicorp’s installation instructions](https://learn.hashicorp.com/terraform/getting-started/install.html) for more details on several methods and a tutorial video, plus the [Microsoft Docs on installing Terraform on the WSL](https://techcommunity.microsoft.com/t5/Azure-Developer-Community-Blog/Configuring-Terraform-on-Windows-10-Linux-Sub-System/ba-p/393845).

![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)**Verification Checklist**

- Terraform is installed and executable from the terminal in whichever folder on the system.

## 2: Azure CLI

For this tutorial, there are several ways for Terraform to authenticate to Azure, I’ll be using the Azure CLI authentication method as detailed in this [tutorial](https://learn.hashicorp.com/terraform/azurerm/authentication-azure-cli) from Hashicorp. There are also some important notes about the Azure CLI. The Azure CLI method in conjunction with the AzureRM Terraform Provider is used to build out resources using infrastructure as code paradigms, because of this it is important also to insure we have the right versions of everything to work together.

*The Caveats*

For the AzureRM, which will be downloaded automatically when we setup the repository and initialize it with the `terraform init` command, we’ll want to make sure we have version 1.20 or greater. Previous versions of the AzureRM Provider used a method of authorizing that reset credentials after an hour. A clear issue.

Terraform also only support authenticating using the `az` CLI and it must be avilable in the path of the system, same as the way `terraform` is available via the path. In other words, if both `terraform` and `az` can be executed from anywhere in the terminal we’re all set. Using the older methods of Powershell Cmdlets or `azure` CLI methods aren’t supported anymore.

Authenticating via the Azure CLI is only supported when using a “User Account” and not via Service Principal (ex: `az login --service-principal`). This works perfectly since these environments I’m building are specifically for my development needs. If you’d like to use this example as a more production focused example, then using something like Service Principals or another systems level verification, authentication, and authorization model should be used. For other examples check out authentication via a [Service Principal and Client Secret](https://learn.hashicorp.com/terraform/azurerm/authentication-service-principal-client-secret.html), [Service Principal and Client Certificate](https://learn.hashicorp.com/terraform/azurerm/authentication-service-principal-client-certificate.html), or [Managed Service Identity](https://learn.hashicorp.com/terraform/azurerm/managed-service-identity.html).

**Installing**

To get the Azure CLI installed I followed the manual installation on [Debian/Ubuntu Linux process](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest). For Windows installation check out [these instructions](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli).

```
# Update the latest packages and make sure certs, curl, https transport, and related packages are updated.
sudo apt-get update
sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg

# Download and install the Microsoft signing key.
curl -sL https://packages.microsoft.com/keys/microsoft.asc | \
    gpg –dearmor | \
    sudo tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null

# Add the software repository of the Azure CLI.
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
    sudo tee /etc/apt/sources.list.d/azure-cli.list

# Update the repository information and install the azure-cli package.
sudo apt-get update
sudo apt-get install azure-cli
```

[View the gist on GitHub](https://gist.github.com/Adron/283fc199a7d0a801f78b63f04f47aaff/55e493a48f2c734976a62dcc532be3d454c430e8/install.sh)

**Login & Setup**

`az login`

It’ll bring up a browser that’ll give you a standard Microsoft auth login for your Azure Account.

![login.png](/wp-content/uploads/2019/08/login.png)

When that completes successfully a response is returned in the terminal as shown.

![loggedin.jpg](/wp-content/uploads/2019/08/loggedin.jpg)

Pieces of this information will be needed later on so I always copy this to a text file for easy access. I usually put this file in a folder I call “DELETE THIS CUZ SECURITY” so that I remember to delete it shortly thereafter so it doesn’t fall into the hands of evil!

For all the other operating systems and places that the Azure CLI can be installed, check out the [docs here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

Once logged in a list of accounts can be retrieved too. Run `az account list` to get the list of accounts available. If you only have one account (re: subscriptions) then you’ll just see exactly what was displayed when you logged in. However if you have other peripheral information, those accounts will be shown here.

If there is more than one subscription, one needs selected and set. To do that execute the following command by passing the subscription id. That’s the second value in that list of values above. Yes, it is kind of odd that they use account and subscription interchangeably in this situation, and that subscription id isn’t exactly obvious if this data is identified as an account and not a subscription, but we’ll give Microsoft a pass for now. Suffice it to say, account id and subscription id in this data is the stand alone id field in the aforementioned data.

`az account set --subscription="id"` where id is subscription id, or as shown in `az account list` the id there, whatever one wants to call it.

**Configuring Terraform Azure CLI Auth**

To do this we will go ahead and setup the initial repository and files. What I’ve done specifically for this is to navigate to Github to the new repository path <https://github.com/new>. Then I selected the following options:

1. Repository Name: terraform-todo-list
2. Description: This is the infrastructure project that I’ll be using to “turn on” and “turn off” my development environment every day.
3. Public Repo
4. I checked *Initialize this repository with a README* and then added the *.gitignore* file with the *Terraform* template, and the *Apache License 2.0*.

![newproject.png](/wp-content/uploads/2019/08/newproject.png)

This repository is now available at <https://github.com/Adron/terraformer-todo-list>. All of the steps and details outlined in this blog entry will be available in this repository plus any of my ongoing work on bastion servers, clusters, kubernetes, or other related items specific to my development needs.

With the repository cloned locally via `git clone git@github.com:Adron/terraformer-todo-list.git` there needs to be a `main.tf` file created. Once created I’ve added the azurerm provider block `provider "azurerm" { version = "=1.27.0" }` into the file. This enables Terraform to be executed from this repository directory with `terraform init`. Running this will pull down the azurerm provider dependency. If everything succeeds you’ll get a response from the command.

![terraform-init-success](/wp-content/uploads/2019/08/terraform-init-success.png)

However if it fails, routinely I’ve ended up out of sync with Terraform version vs. provider version. As mentioned above we definitely need 1.20.0 or greater for the examples in this post. However, I’m also running Terraform at version 0.12.6 which requires at least 1.27.0 of the azurerm or better. If you see an error like this, it’s usually informative and you’ll just need to change the version number so the version of Terraform you’re using will pull down the right version.

![terraform-init-fail](/wp-content/uploads/2019/08/terraform-init-fail.png)

Next I run `terraform plan` and everything should respond with no change to infrastructure requested response.

![terraform-plan-aok.png](/wp-content/uploads/2019/08/terraform-plan-aok.png)

At this point I want to verify authentication against my Azure account with my Terraform CLI, to do this there are two additional fields that need to be added to the provider: *subscription\_id* and *tenant\_id*. The configuration will look similar to this, except with the subscription id and tenant id from the `az account list` data that was retrieved earlier when setting up and finding the the Azure account details from the Azure CLI.

![terraform-main-auth](/wp-content/uploads/2019/08/terraform-main-auth.png)

Run `terraform plan` again to see the authentication results, which will look just like the `terraform plan` results above. With this done there’s just one more thing to do so that we have a good work space in which to work with Terraform against Azure. I always, at this point of any project with Terraform and Azure, setup a [Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview).

![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)**Verification Checklist**

- Terraform is installed and executable from the terminal in whichever folder on the system.
- Azure CLI is installed and executable from the terminal in whichever folder on the system.
- The Azure CLI has been used to login to the Azure account and the subscription/account set for use as the default subscription/account for the Azure CLI commands.
- A repository has been setup on Github (here) that has a main.tf file that I used to create a single Azure Resource Group in which to do future work within.

## **3: Azure Resource Group**

Just for clarity, a few details about the resource group. A Resource Group in Azure is a grouping that should share the same lifecycle, which is exactly what I’m aiming to do with all of these resources on a day to day basis for development. Every day I intend to start these resources in this Resource Group and then shut them all down at the end of the day.

There are other specifics about what exactly a Resource Group is, but I’ll leave the [documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview) to be read to elaborate further, for my mission today I just want to have a Resource Group available for further Terraform work. In Terraform the way I go about creating a Resource Group is by adding the following to my `main.tf` file.

```
provider "azurerm" {
  version = "=1.27.0"

  subscription_id = "00000000-0000-0000-0000-000000000000"
  tenant_id       = "11111111-1111-1111-1111-111111111111"

}

resource "azurerm_resource_group" "adrons_resource_group_workspace" {
  name     = "adrons_workspace"
  location = "West US 2"

  tags = {
    environment = "Development"
  }
}
```

[View the gist on GitHub](https://gist.github.com/Adron/99a5a5a795179aac2a0a8c007efcaf20/743f90e4001a22fd6fcea3300280ad60e69ff224/main.tf)

Run `terraform plan` to see the changes. Then run `terraform apply` to make the changes, which will need a confirmation of `yes`.

![terraform-apply-done](/wp-content/uploads/2019/08/terraform-apply-done.png)

Once I’m done with that I go ahead and issue a `terraform destroy` command, giving it a `yes` confirmation when asked, to destroy and wrap up this work for now.

![terraform-destroy-cleanup](/wp-content/uploads/2019/08/terraform-destroy-cleanup.png)

![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)**Verification Checklist**

- Terraform is installed and executable from the terminal in whichever folder on the system.
- Azure CLI is installed and executable from the terminal in whichever folder on the system.
- The Azure CLI has been used to login to the Azure account and the subscription/account set for use as the default subscription/account for the Azure CLI commands.
- A repository has been setup on Github (here) that has a main.tf file that I used to create a single Azure Resource Group in which to do future work within.
- I ran `terraform destroy` to clean up for this set of work.

## 4: Using Environment Variables

There is one more thing before I want to commit this code to the repository. I need to get the subscription id and tenant id out of the main.tf file. One wouldn’t want to post their cloud access and identification information to a public repository, or ideally to any repository. The easy fix for this is to implement some interpolated variables to pull from environment variables. I can then set the [environment variables](https://www.terraform.io/docs/commands/environment-variables.html) via my startup script (*such as [.bash\_profile or .bashrc](/2018/11/06/bash-a-k-a-the-solution-for-everything-a-few-of-the-special-files/) or even the IDE I’m running the Terraform from like [Intellij](https://www.jetbrains.com/idea/) or [Webstorm](https://www.jetbrains.com/webstorm/) for example*). In that script setting the variables would look something like this.

```
export TF_VAR_subscription_id="00000000-0000-0000-0000-000000000000"
export TF_VAR_tenant_id="11111111-1111-1111-1111-111111111111"
```

[View the gist on GitHub](https://gist.github.com/Adron/ab6815269a7eda6cae80b0571546b870/f82ce5798817651fa27d5f92b5fca9830c4c7269/.bash_profile.sh)

Note that each variable is prepended with `TF_VAR`. This is the convention so that Terraform will look through and pick up all of the variables that it needs to work with. Once these variables are added to the startup script, run a `source ~/.bashrc` (linux) or `source ~/.bash_profile` (on Mac) to set those variables.  For Windows check out [this](https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt) to set the environment variables. With that set there are a few more steps.

In the repository create a file named `variables.tf` and add the two variables `variable "subscription_id" {}` and `variable "tenant_id" {}`. Then in the `main.tf` file change the subscription\_id and tenant\_id fields to be assigned variables like `subscription_id = var.subscription_id` and `tenant_id = var.tenant_id`. Now run `terraform plan` and these results should display.

![terraform-plan-after-variables](/wp-content/uploads/2019/08/terraform-plan-after-variables.png)

Now the `terraform apply` can be applied or `terraform destroy` to create or destroy the Resource Group. The last step now is to just commit this infrastructure code with the variables now removed from the main.tf file.

`git add -A`

`git commit -m 'First executable resource.'`

`git rebase` to pull in all the remote default files and such and merge those with the local additions.

`git push -u origin master` then to push the changes and set the master local branch to track with the remote branch master.

![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)**Verification Checklist**

- Terraform is installed and executable from the terminal in whichever folder on the system.
- Azure CLI is installed and executable from the terminal in whichever folder on the system.
- The Azure CLI has been used to login to the Azure account and the subscription/account set for use as the default subscription/account for the Azure CLI commands.
- A repository has been setup on Github (here) that has a main.tf file that I used to create a single Azure Resource Group in which to do future work within.
- I ran `terraform destroy` to clean up for this set of work.
- Private sensitive data has been moved from the main.tf file into environment variables so that it isn’t copied to the repository.
- A variables.tf file has been added for the aforementioned variables that map to environment variables.
- The code base has been committed to Github at <https://github.com/Adron/terraformer-todo-list>.
- Both `terraform plan` and `terraform apply` deploy as expected and `terraform destroy` removes infrastructure cleanly as expected.

Next steps coming soon!
