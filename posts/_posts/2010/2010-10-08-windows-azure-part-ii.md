---
title: What You Need and Want With Windows Azure Part II
date: 2010-10-08 05:15:18 -0700
last_modified_at: 2010-10-07 22:08:39 -0700
permalink: /2010/10/08/windows-azure-part-ii/
slug: windows-azure-part-ii
wp_id: 1440
original_url: https://compositecode.blog/2010/10/08/windows-azure-part-ii/
categories:
- Azure
- How-to
tags:
- azure
- BLOB
- BLOB container
- cloud
- cloud computing
- cloud service
- cloud storage
- microsoft
- windows azure
excerpt: One of the most useful tools to use in Windows Azure Development is the Windows Azure MMC. The Microsoft Management Console, or MMC, is the management console that many of the Windows Server Management interfaces can plug into. The Windows Azure Team has put together the Windows Azure specific MMC Console Plugin that is available for download on Microsoft MSDN Code Site at http://code.msdn.microsoft.com/windowsazuremmc . Windows Azure MMC Code Site When you navigate to the page, click on the tab for downloads and you will find three different files; WindowsAzureMMC.exe PerfMon-Friendly Log Viewer Plugin PerfMon-Friendly Log Viewer Plugin (Source Only) The main file you’ll need to download is the WindowsAzureMMC.exe file. Once this file is downloaded, run the executable. An installation wizard will appear, just click next and step through each of the steps accepting any defaults. Windows Azure Management Tool Installation Once the executable runs…
---

One of the most useful tools to use in Windows Azure Development is the [Windows Azure MMC](http://code.msdn.microsoft.com/windowsazuremmc).  The Microsoft Management Console, or MMC, is the management console that many of the Windows Server Management interfaces can plug into.  The Windows Azure Team has put together the Windows Azure specific MMC Console Plugin that is available for download on Microsoft MSDN Code Site at <http://code.msdn.microsoft.com/windowsazuremmc>.

[![Windows Azure MMC Code Site](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-007/1038284119_pdqwL-S.png "Windows Azure MMC Code Site")](http://code.msdn.microsoft.com/windowsazuremmc)

*Windows Azure MMC Code Site*

When you navigate to the page, click on the tab for downloads and you will find three different files;

- WindowsAzureMMC.exe
- PerfMon-Friendly Log Viewer Plugin
- PerfMon-Friendly Log Viewer Plugin (Source Only)

The main file you’ll need to download is the WindowsAzureMMC.exe file.  Once this file is downloaded, run the executable.  An installation wizard will appear, just click next and step through each of the steps accepting any defaults.

[![Windows Azure Management Tool Installation](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-008/1038284135_eDnyk-S.png "Windows Azure Management Tool Installation")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-008/1038284135_eDnyk-O.png)

*Windows Azure Management Tool Installation*

Once the executable runs it should pop up a Windows Explorer Window, if not navigate to where the files where just installed (unzipped) to.  By default the installer places them in C:\WindowsAzureMMC\.  Find the file StartHere.cmd located in the installation directory and fun the file.

[![StartHere.cmd ](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-009/1038289552_kxdjy-S.png "StartHere.cmd")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-009/1038289552_kxdjy-O.png)

*StartHere.cmd*

When the file is executed a DOS prompt will flicker, and another configuration wizard titled Windows Azure Management Tools will appear.

[![Configuration Wizard for the Windows Azure Management Tools](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-010/1038289636_56T74-S.png "Configuration Wizard for the Windows Azure Management Tools")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-010/1038289636_56T74-O.png)

*Configuration Wizard for the Windows Azure Management Tools*

Click next and the installation will start, checking each of the dependencies required to execute the MMC.

[![Detecting Required Software](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-011/1038289643_nWoZM-S.png "Detecting Required Software")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-011/1038289643_nWoZM-O.png)

*Detecting Required Software*

Continue to click any next prompts, and then you will have the Windows Azure MMC Console open once the StartHere.cmd finishes executing.  Click close on the configuration wizard.

[![Installation Completed](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-012/1038289654_EkHsE-S.png "Installation Completed")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-012/1038289654_EkHsE-O.png)

*Installation Completed*

The MMC will now be displayed on screen as shown below.

[![Windows Azure Management Tool (MMC)](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-013/1038300817_WKGW7-S.png "Windows Azure Management Tool (MMC)")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-013/1038300817_WKGW7-O.png)

*Windows Azure Management Tool (MMC)*

Open the Windows Azure Management section by clicking on the small tree view arrow on the left hand side.  The tree view will open up to a Service Management Node with a Hosted Services, Storage Services, and Affinity Groups listed underneath the node.  Select the actual Service Management Node so that the middle window shows the connection form shown here.

[![Windows Azure MMC Services Management Node Connection](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-014/1038300866_xTsE4-S.png "Windows Azure MMC Services Management Node Connection")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-014/1038300866_xTsE4-O.png)

*Windows Azure MMC Services Management Node Connection*

Now navigate back to Windows Azure Platform Web Interface (<http://windows.azure.com>).  Click on the project displayed on the main screen to select it.

[![Windows Azure Portland Interface](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-022-suggested-cropping/1038304637_vWMgk-S.png "Windows Azure Portland Interface")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-022-suggested-cropping/1038304637_vWMgk-O.png)

*Windows Azure Portland Interface*

When the follow page displays, click on the Account tab at the center top of the page.

[![Windows Azure Project](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-023-suggested-cropping/1038308451_V8Xzg-S.png "Windows Azure Project")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-023-suggested-cropping/1038308451_V8Xzg-O.png)

*Windows Azure Project*

When the Account Page finishes rendering look at the very bottom to locate the subscription ID.

[![Windows Azure Project Account Properties](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-018-suggested-cropping/1038308416_9Bkb6-S.png "Windows Azure Project Account Properties")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-018-suggested-cropping/1038308416_9Bkb6-O.png)

*Windows Azure Project Account Properties*

Enter the subscription ID into the form.  Now click on the ellipsis button on the form so the certificates that are available are displayed.

[![API Certificate](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-016/1038310404_HCGKV-S.png "API Certificate")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-016/1038310404_HCGKV-O.png)

*API Certificate*

Click on the underlined link on the certificate you want to use (sometimes there are a few options, depending on what is installed on the machine already).  A properties dialog should appear when you click on the underlined link button.

[![Certificate Details](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-025/1038308462_4fEK2-S.png "Certificate Details")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-025/1038308462_4fEK2-O.png)

*Certificate Details*

Click on the Details Tab on the top of the properties dialog window.

[![Certificate Details, Details Tab](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-026/1038317489_2GoC2-S.png "Certificate Details, Details Tab")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-026/1038317489_2GoC2-O.png)

*Certificate Details, Details Tab*

Now click on the Copy to File Button.  An export process will start for the certificate.  Click on next.  On the next screen make sure No, do not export the private key is selected.  The next screen selects the DER encoded binary X.509 (.CER) option.  Verify this setting and then click next.

[![Certificate Export Wizard](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-027/1038308492_2puWk-S.png "Certificate Export Wizard")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-027/1038308492_2puWk-O.png)

*Certificate Export Wizard*

Click on next and then enter the path and filename where you want to save the certificate.

[![Save As File Name for Certificate](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-028/1038308491_qaamT-S.png "Save As File Name for Certificate")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-028/1038308491_qaamT-O.png)

*Save As File Name for Certificate*

Now that you have the certificate, return to the Windows Azure Platform Web Interface (<http://windows.azure.com>).  Navigate to the Account Tab section of the site again.  On that page click on the Manage My API Certificates.  This is the same page as shown above in the image captioned “*Windows Azure Project Account Properties*“.  Once the page displays click on the Choose File button on the page.  Find the location the certificate was saved and select the certificate.  Now click the upload button to upload the file to the Windows Azure Account.

[![API Certificates Upload](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-019-suggested-cropping/1038308432_ykvPH-S.png "API Certificates Upload")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-019-suggested-cropping/1038308432_ykvPH-O.png)

*API Certificates Upload*

When the file is done uploading the page will update and show something similar to what is shown in the next screenshot.

[![API Certificates, Finished Uploading](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-020-suggested-cropping/1038308442_ePBef-S.png "API Certificates, Finished Uploading")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-020-suggested-cropping/1038308442_ePBef-O.png)

*API Certificates, Finished Uploading*

Now you can click on the OK button, if you haven’t already, to confirm the API Certificate in the Windows Azure MMC.  Click on the Connect button in the far right window area of the MMC.  It should take a second but the connection should occur.  You can tell by the Default storage account form drop down becomes enabled.  At this time though, since we haven’t placed anything in storage or started any storage services there will be nothing displayed in the drop down.

At this point the MMC is functional; there just isn’t much to look at in the Windows Azure Account yet.  So let’s change that and setup some sample services.  First head back over to the Windows Azure Platform Web Interface (<http://windows.azure.com>).  Once you’re in click on the project as we did before so that it is the focus point.  Click on the +New Service link in the top right of the main page window section.

[![Starting a Windows Azure Service](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-029-suggested-cropping/1038367916_aXEF8-S.png "Starting a Windows Azure Service")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-029-suggested-cropping/1038367916_aXEF8-O.png)

*Starting a Windows Azure Service*

The next screen will display the options to create a Windows Azure Storage Account or a Hosted Services Role.  Click on the Windows Azure Storage Account option.

[![Windows Azure Create a Service](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-030-suggested-cropping/1038383398_4KorE-S.png "Windows Azure Create a Service")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-030-suggested-cropping/1038383398_4KorE-O.png)

*Windows Azure Create a Service*

On the screen that renders fill out the service label and description.  Both of these fields are mostly free text, allowing spaces and special characters.  Click next when you have filled out the label and description.

[![Services Properties](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-031-suggested-cropping/1038383414_hrvr9-S.png "Services Properties")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-031-suggested-cropping/1038383414_hrvr9-O.png)

*Services Properties*

The next form that comes up has the public storage account name.  This field must be compliant with URI naming conventions.  The idea also is that these storage services use a RESTful API, it is best to follow the REST Architecture ideals and name the location something easy to read and to remember.  You can click the check availability button to verify if the name is used or not.  If it is available move down and select Anywhere US for the region.

[![First Storage Sample](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-032-suggested-cropping/1038383421_CjmWS-S.png "First Storage Sample")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-032-suggested-cropping/1038383421_CjmWS-O.png)

*First Storage Sample*

Once you are finished click the create button at the bottom of the form.  The next window will render the results of creating the Windows Azure Storage Account.  This page has all the information you’ll need to fill out the Windows Azure MMC connection information.

[![Windows Azure Storage Account Properties](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-033-suggested-cropping/1038383440_Ez3xh-S.png "Windows Azure Storage Account Properties")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-033-suggested-cropping/1038383440_Ez3xh-O.png)

*Windows Azure Storage Account Properties*

If you still have the Windows Azure MMC open, bring focus to it again.  If not open it back up and open the Windows Azure Management tree view back to the Service Management Node and verify or enter the information for the subscription ID and API Certificate.  Now click on the Connect link button on the right hand window pane.  The MMC will then connect and will populate the Default storage account drop down.  Click on the drop down and you will see your Windows Azure Storage Account that we just created.

[![Service Management Node Connected with Default Storage Account](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-034/1038424995_rb9ag-S.png "Service Management Node Connected with Default Storage Account")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-034/1038424995_rb9ag-O.png)

*Service Management Node Connected with Default Storage Account*

Now that we have a Windows Azure Storage Account, let’s get a Windows Azure Services Role running also.  Navigate back to the Windows Azure Platform Web Interface (<http://windows.azure.com>).  Once the page has rendered click on your specific project, wait for that page to render and  then on the +New Service link. This time select the Windows Azure Services Role to create.  On the next page fill out the service label and description the same as with the Windows Azure Storage Account creation.

[![Create a Service (Role)](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-036-suggested-cropping/1038425020_jmhry-S.png "Create a Service (Role)")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-036-suggested-cropping/1038425020_jmhry-O.png)

*Create a Service (Role)*

Click next when complete.  On the next page that renders you’ll again pick a public URI subdomain path, which I’ve used firstservicesample as mine, and select Anywhere US from the drop down for the region.  Click on the create button when complete.  The following page will display with a single cube image in the center of the screen, label Production.  For now, the instance role is available, but nothing is deployed and nothing is being charged at this time.  However this is perfect for checking out the Windows Azure MMC display of the services.

[![Service Role](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-038-suggested-cropping/1038425044_a9zDR-S.png "Service Role")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-038-suggested-cropping/1038425044_a9zDR-O.png)

*Service Role*

Return to the Windows Azure MMC and click on the Hosted Services node.  Click on Connect in the right hand window pane under actions.  The firstservicesample node, or whatever you may have named the service, will display with the staging, production, and certificates nodes appearing below.  From here you can deploy, upgrade, run, delete, suspend, swap, or even save the configuration of your roles.  This is extremely helpful so that one doesn’t always need to return to the site and can maintain multiple hosted services, storage services, affinity groups, and more from the MMC.

[![Windows Azure Staging](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-039/1038425080_xHcgS-S.png "Windows Azure Staging")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-039/1038425080_xHcgS-O.png)

*Windows Azure Staging*

Next let’s click on the Storage Explorer Node just below the Service Management Node.  Click on New Connection and enter the Account Name as shown below.

[![New Account Form](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-043/1038425082_pJh9F-O.png "New Account Form")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-043/1038425082_pJh9F-O.png)

*New Account Form*

Now that the account name and URIs are filled out.  Return to the storage services properties page in the Windows Azure Platform Web Interface (<http://windows.azure.com>).

[![Windows Azure Storage Account Properties](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-033-suggested-cropping/1038383440_Ez3xh-S.png "Windows Azure Storage Account Properties")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-033-suggested-cropping/1038383440_Ez3xh-O.png)

*Windows Azure Storage Account Properties*

On this page you’ll find the key you need to finish off the form in the Windows Azure MMC.  Once you’ve completed the form click on OK.  The MMC should now populate out the cloud storage account area with a node for BLOB Containers.

[![Storage Account Services](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-044/1038480997_u3oRC-S.png "Storage Account Services")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-044/1038480997_u3oRC-O.png)

*Storage Account Services*

Click on the BLOG Containers so and click on Add Container in the right hand side window pane under actions.  Enter a name, in this case I entered musicmanager, and click OK.  Now you should have a BLOB Storage Container in your Windows Azure Storage Account.

[![Windows Azure BLOB Container](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-045/1038481093_MGFA3-S.png "Windows Azure BLOB Container")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-045/1038481093_MGFA3-O.png)

*Windows Azure BLOB Container*

Click on the musicmanager BLOB Container, or whatever you named yours, and then click on Upload BLOB under the actions window on the right hand side.  Select a file, I’ve chosen a music MP3 I have on my local machine.

[![Uploading a BLOG File (A Music MP3)](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-046/1038481199_oDKtg-S.png "Uploading a BLOG File (A Music MP3)")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-046/1038481199_oDKtg-O.png)

*Uploading a BLOG File (A Music MP3)*

Click OK and you’ll see the Operations queue node on the lower left hand side of the Console Root tree view populate with the upload activity task.

[![The Upload in the Operations Queue](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-047/1038481215_s2wFr-S.png "The Upload in the Operations Queue")](/images/photos.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-047/1038481215_s2wFr-O.png)

*The Upload in the Operations Queue*

After the upload is complete the BLOB Container will then show the BLOBs just below it when selected in the Windows Azure MMC.
