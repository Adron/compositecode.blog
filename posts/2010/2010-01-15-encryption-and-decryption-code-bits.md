---
title: Encryption and Decryption Code Bits
date: 2010-01-15 00:33:00 +0000
last_modified_at: 2010-01-15 00:33:00 +0000
permalink: /2010/01/15/encryption-and-decryption-code-bits/
slug: encryption-and-decryption-code-bits
wp_id: 683
original_url: https://compositecode.blog/2010/01/15/encryption-and-decryption-code-bits/
categories:
- Uncategorized Bits
tags: []
excerpt: I recently had to do some simple encryption and decryption for password storage. I wanted to document this so a blog entry seemed in order. So without any yammering here’s the simple class I created. public static class EncryptionHelper { private const string CryptographyKey = "CryptKey"; // The Initialization Vector for the DES encryption routine …
---

I recently had to do some simple encryption and decryption for password storage.  I wanted to document this so a blog entry seemed in order.  So without any yammering here’s the simple class I created.

```
public static class EncryptionHelper
    {
        private const string CryptographyKey = "CryptKey";

        // The Initialization Vector for the DES encryption routine
        private static readonly byte[] iv =
            new byte[] { 220, 13, 41, 29, 1, 63, 73, 9 };

        /// <summary>
        /// Encrypts provided string parameter
        /// </summary>
        public static string Encrypt(string s)
        {
            if (string.IsNullOrEmpty(s)) return string.Empty;

            byte[] buffer = Encoding.ASCII.GetBytes(s);
            var des = new TripleDESCryptoServiceProvider();
            var md5 = new MD5CryptoServiceProvider();

            des.Key = md5.ComputeHash(Encoding.ASCII.GetBytes(CryptographyKey));
            des.IV = iv;

            string result = Convert.ToBase64String(
                des.CreateEncryptor().TransformFinalBlock(
                    buffer, 0, buffer.Length));

            return result;
        }

        /// <summary>
        /// Decrypts provided string parameter
        /// </summary>
        public static string Decrypt(string s)
        {
            if (string.IsNullOrEmpty(s)) return string.Empty;

            byte[] buffer = Convert.FromBase64String(s);
            var des = new TripleDESCryptoServiceProvider();
            var md5 = new MD5CryptoServiceProvider();

            des.Key = md5.ComputeHash(Encoding.ASCII.GetBytes(CryptographyKey));
            des.IV = iv;

            string result = Encoding.ASCII.GetString(
                des.CreateDecryptor().TransformFinalBlock(
                    buffer, 0, buffer.Length));

            return result;
        }
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

So simple enough.  Hope that is helpful to anyone interested in a super easy encrypt & decrypt example.  : )
