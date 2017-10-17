---
slug: "47"
layout: content-2-panel
title: Crawling Module Configuration
categories: migrated
---

# Crawling Module Configuration

Note:

> The Coveo Cloud V2 Crawling Module is currently in an alpha version and must be configured with the Coveo Support assistance.

 

You need to configure your Crawling Module instance to specify details about the repository and the content to index.

1.  If not already done, create a secured push type source and get an API key (see [Creating a Push Type Source](https://developers.coveo.com/x/uIQAAg)).
2.  Ensure that your API key has the appropriate privileges. 
    In the administration console API Access page, select the View check boxes for the following ones:
    1.  **Security identities**
    2.  **Security identity providers**
    3.  **Sources**

    When you want to control from which machines your API key is authorized to be used, you can always whitelist or blacklist machines from the administration console (see API Access - Page).
3.  Get the organizationId and sourceId (see Parameters and API Calls).
    In the administration console Sources page, once the Status of your source is Ready to receive items, copy your organizationId and sourceId that appear under the source name.

    **Example:**

    If your organization name is **Coveo Search**, as shown in the capture below, your `organizationId` would be `coveosearch` and the `sourceId` for this source would be `coveosearch-stx6y2vdtd2xo6l7cxhlmpsmdu`.

    ![](attachments/35489765/35455210.png)

4.  Edit the content of the `your_working_folder\crawler.json` file.

    In the file, remove all the blade definitions except the crawlerBlade blade definition: 

    **Example:**

    For the File crawler taken from the `FileSystemInstanceTemplate.zip` file:

    ```
    {
        "blade":{
            "name":"File Crawler",
            "type":"CrawlerBlade@CIDXCrawlerBlade8.dll",
            "serves":"http://localhost:52840/ServiceURI/ICrawler",
            "PushApiScriptPath":"C:\Crawling_module/your_working_folder/bin/push_api_blade.py",
            "PushApiBlobStoreScriptPath":"C:\Crawling_module/your_working_folder/bin/push_api_blobstore.py",
            "reporting":"ReportingServiceUri",
            "CrawlerName":"CESCC.DotNetCrawler#File System",
            "AssemblyPath":"Coveo.CES.CustomCrawlers.File.dll",
            "AssemblyType":"Coveo.CES.CustomCrawlers.File.FileCrawler"
        }
    }
    ```

    If you installed more than one Crawling Module instance on this Windows server, change the default port value (`52840`) to a value used exclusively by this instance.  

5.  Replace the content of `your_working_folder\CmfAutoConfig.json` file by the following code line:

    ```
    { _type : Coveo.CmfAdmin.CmfConfig }
    ```

6.  Edit the `your_working_Folder\Logger.json` file to only contain one `Log` object in the `Logs` list:

    ```
    ... 
    Logs:[
        { 
            _type:Coveo.LogConfig.LogToFile, 
            Path:'./Log', 
            FileName:'Crawlers.log', 
            UseDate:True, 
            MinimumSeverity:Normal, 
            UpdateInBackground: True, 
            Verbose:False
        }
    ] 
    ...
    ```

7.  Customize the` your_working_folder\Config.json` file:

    1.  Replace all `CHANGE_ME` by their real values.

        <table>
        <colgroup>
        <col width="50%" />
        <col width="50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th>Key</th>
        <th>Value</th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><code>Config.IndexIdentifier</code></td>
        <td><p>A Coveo Cloud index identifier for the index of your organization.</p>
        <div class="aui-message warning shadowed information-macro">
        <div class="message-content">
        <blockquote>
        The <code>Config.IndexIdentifier</code> parameter is currently required for the Crawling Module configuration, but its value can be anything (e.g.: <code style="line-height: 1.42857;background-color: transparent;">anything</code>).
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="even">
        <td><code>Config.SourceInformation.SourceName</code></td>
        <td>The name of the Coveo Cloud source in which the content will be pushed, as it appears in the Coveo Cloud Administration Console <strong>Sources</strong> page.</td>
        </tr>
        <tr class="odd">
        <td><code>Config.StartingAddresses</code></td>
        <td><p>The URL or address where the connector starts to crawl. The format depends on the connector type. Refer to the CES 7.0 connector documentation to find the information<br />
        (e.g.: For a File connector the starting address can be: <code class="java plain">file:</code><code class="java comments">///C:/Onprem/FileCrawlerV42/PushSource</code>).</p>
        <div class="aui-message hint shadowed information-macro has-no-icon">
        <p>Tip:</p>
        <div class="message-content">
        <blockquote>
        In <a href="https://search.coveo.com">search.coveo.com</a>, you can search for &quot;configuring and indexing&quot; connector &quot;starting address&quot; and add the connector type as a keyword to find the appropriate connector topic describing requirements for the <strong>Starting Address</strong> parameter value.
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="even">
        <td><code>Config.Parameters.PushAuthorizationToken</code></td>
        <td><p>Your valid API key with appropriate privileges</p></td>
        </tr>
        <tr class="odd">
        <td><code>Config.Parameters.OrganizationId</code></td>
        <td>The organization identifier (<code>organizationId</code>) (see <a href="Parameters_and_API_Calls">Parameters and API Calls</a>)</td>
        </tr>
        <tr class="even">
        <td><code>Config.Parameters.SourceId</code></td>
        <td>The source identifier (<code>sourceId</code>) (e.g.: <code>coveosearch-syaj2elbj4nlkwybxgxz2l2bdi</code>) (see <a href="Parameters_and_API_Calls">Parameters and API Calls</a>)</td>
        </tr>
        <tr class="odd">
        <td><code>Config.DbConnectionString</code></td>
        <td>A valid connection string to your local MySQL instance (e.g.: <code>Server=localhost;Uid=root;Pwd=your_first_name;Database=MyOrg;</code>)</td>
        </tr>
        </tbody>
        </table>

    2.  Ensure that the following parameters have the proper values:

        <table>
        <colgroup>
        <col width="50%" />
        <col width="50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th>Key</th>
        <th>Value</th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><code>Config.SourceSecurityOption</code></td>
        <td><p>The default value is <code>Retrieve</code>, meaning the permissions are retrieved from the repository for each item (see <a href="http://www.coveo.com/go?dest=ccv2ac&amp;context=31">Source Permission Types</a>).</p>
        <p>The possible values are:</p>
        <p><code>Retrieve</code> - The Crawling Module retrieves permissions for each repository item. This is similar to a <strong>Secured</strong> type source configuration in the Coveo Cloud Administration Console.</p>
        <p><code>Specified</code> - The Crawling Module does nothing about permissions at the item level. The permissions must be set at the source level as <strong>Shared</strong> or <strong>Private</strong> in the Coveo Cloud Administration Console.</p></td>
        </tr>
        <tr class="even">
        <td><code>Config.SourceInformation.SourceId</code></td>
        <td><p>A Crawling Module internal numeric unique ID between all on-premises Crawling Module instances that use the same MySQL database (e.g.: <code>1</code>).</p>
        <div class="aui-message warning shadowed information-macro">
        <div class="message-content">
        <blockquote>
        Do not confuse this database <code>SourceId</code> parameter with the Coveo Cloud Organization source ID (<code>Config.Parameters.SourceId</code> parameter).
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="odd">
        <td><code>Config.BlobStoreUri</code></td>
        <td>Must be: <code>./BlobStore</code></td>
        </tr>
        <tr class="even">
        <td><code>Config.DocumentConsumerUri</code></td>
        <td>Must be: <code>./PushApi</code></td>
        </tr>
        <tr class="odd">
        <td><code>Config.Parameters.PushUri</code></td>
        <td>Must be:<code>https://push.cloud.coveo.com/v1</code></td>
        </tr>
        <tr class="even">
        <td><code>Config.Parameters.PushUseBatch</code></td>
        <td><p>[Optional] Boolean used to push items in a batch.</p>
        <p>Set the parameter to true to enable batch mode.</p>
        <div class="code panel pdl" style="border-width: 1px;">
        <div class="codeHeader panelHeader pdl" style="border-bottom-width: 1px;">
        <strong>Example</strong>
        </div>
        <div class="codeContent panelContent pdl">
        <pre style="font-size:12px;"><code>{
            ...
            &quot;Parameters&quot;: {
                &quot;PushUseBatch&quot;: {
                    &quot;Value&quot;: true
                }
            }
            ...
        }</code></pre>
        </div>
        </div></td>
        </tr>
        </tbody>
        </table>

    3.  When crawling permissions, add a security identity provider.

        The specified security provider must be the type expected by the crawler.

        **Example:**

        The File crawler needs the Active Directory security provider:

        ```
        ... "SecurityProviders": { "SecurityProvider": { "TypeName": "Active Directory", "_type": "Coveo.SecurityProvider", "Name": "Active Directory" } } ...
        ```

        Tip:

        > In [search.coveo.com](https://search.coveo.com/), you can search for @title="configuring and indexing" "security provider" and add the connector type as a keyword to get the appropriate source configuration topic, and then look for the **Security Provider** parameter description.

8.  Register your Crawling Module instance.
    Run a command like the following to run your Crawling Module as a Windows service.

    ```
    C:\Crawling_module\your_working_folder\bin\CDFNodeProcess8.exe -inlineFile=crawler.json -logConfigFile=logger.json -service=register -ServiceName=CHANGE_ME -ServiceDisplayName=CHANGE_ME -path=C:/Crawling_module/your_working_folder
    ```

    It is strongly recommended to use a meaningful `ServiceName` for your instance.

    **Example**

    ```
    C:\Crawling_module\your_working_folder\bin\CDFNodeProcess8.exe -inlineFile=crawler.json -logConfigFile=logger.json -service=register -ServiceName=CoveoFile -ServiceDisplayName=CoveoFile -path=C:/Crawling_module/your_working_folder
    ```

9.  Start your instance and set its configuration.
    Run the following command:

    ```
    C:\Crawling_module\your_working_folder\bin\crawler.py [-port CHANGE_ME] -setconfig C:\Crawling_module\your_working_folder\Config.json
    ```

    where you replace `CHANGE_ME` by your port.

    > You must run this command each time you modify the `Config.json` file.

#### What's Next

When you want to push on-premises items with permissions, configure a permission expansion tool (see [Configuring a Permission Expansion Tool for a Secured Source](https://developers.coveo.com/x/5IYkAg)).

 
