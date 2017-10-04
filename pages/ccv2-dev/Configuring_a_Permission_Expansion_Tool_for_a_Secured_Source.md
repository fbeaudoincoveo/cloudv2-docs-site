---
layout: content-2-panel
title: Configuring a Permission Expansion Tool for a Secured Source
categories: migrated
---

# Configuring a Permission Expansion Tool for a Secured Source

Note:

> The Coveo Cloud V2 Permission Expansion Tool is currently in an alpha version and must be installed with the assistance of the [Coveo Support](https://coveocommunity.force.com/).

When you want to index item permissions, you must also configure a Permission Expansion Tool.

The Permission Expansion Tool role is to expand group members and identity mappings for an on-premises security identity provider.

> If the on-premises item permissions can be resolved by a cloud provider, do not configure a Permission Expansion Tool. For example, when your Crawling Module already sets Email permissions, you can simply associate an existing Email provider with your source.

 

1.  Before installing the package, in your Crawling Module configuration file, ensure that the Config.SourceSecurityOption parameter is set to Retrieve.

2.  Get the Permission Expansion Tool package.

    Note:

    > Currently, the Permission Expansion Tool package is in an alpha version so you need to contact your client executive to get the ZIP file.

3.  Install the package:
    1.  On the same Windows server as the Crawling Module, create a new folder for the Permission Expansion Tool (example: `C:\Permission_expansion_tool\your_working_folder`).
    2.  In `your_working_folder`, unzip the `SecurityProvidersComponentPackage.zip` file.

    3.  When your repository to index is a database and the targeted database driver is in 32-bit architecture, in `your_working_folder\bin\`, unzip the `your_working_folder\bin\Win32ConnectorUtilities.zip` file.
        The  folder `Win32` appears.

4.  Configure the Permission Expansion Tool:

    1.  In `your_working_folder`, create a JSON configuration file named `Config.json` for the Permission Expansion Tool.

    2.  In your `your_working_folder\Config.json`, when using an `Active Directory` provider, add something like this:

        **Example**

        ```
        {
          "OrganizationId": "CHANGE_ME",
          "ProviderId": "CHANGE_ME",
          "PlatformApiUrl": "https://platform.cloud.coveo.com",
          "PushApiUrl": "https://push.cloud.coveo.com/v1",
          "ApiKey": "CHANGE_ME",
          "SecurityProviders": [
            {
              "Name": "CHANGE_ME",
              "Type": "Active Directory",
              "ProviderBladeType": "Active Directory@CSPWindows8D.dll",
              "SetConfiguration": {
                "Name": "CHANGE_ME",
                "SecurityProviders": {
                  "email_provider": {
                    "TypeName": "Email",
                    "Name": "Email Security Provider"
                  }
                }
              }
            }
          ]
        }
        ```

        where you replace all CHANGE\_ME with their real values:

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
        <td><code>OrganizationId</code></td>
        <td>The organization identifier (see <a href="https://developers.coveo.com/x/QokkAg">Getting the Organization and Source IDs</a>)</td>
        </tr>
        <tr class="even">
        <td><code>ProviderId</code></td>
        <td>The name of the provider you created</td>
        </tr>
        <tr class="odd">
        <td><code>ApiKey</code></td>
        <td><p>A valid API key</p>
        <div class="aui-message warning shadowed information-macro">
        <div class="message-content">
        <blockquote>
        Ensure that your API key has the appropriate privileges:
        </blockquote>
        <blockquote>
        In the administration console <strong>API Access</strong> page, select your <strong>API key</strong>, and in the <strong>Privileges</strong> tab, select the <strong>View</strong> check boxes for the following privileges:
        </blockquote>
        <blockquote>
        a. <strong>Security identities</strong>
        </blockquote>
        <blockquote>
        b. <strong>Security identity providers</strong>
        </blockquote>
        <blockquote>
        c. <strong>Sources</strong>
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="even">
        <td><code>SecurityProviders.Name</code></td>
        <td>The name of the on-premises provider</td>
        </tr>
        <tr class="odd">
        <td><code>SecurityProviders.SetConfiguration.Name</code></td>
        <td>The name of the on-premises provider</td>
        </tr>
        </tbody>
        </table>

        > If you are using another type of provider, unzip the `your_working_folder\bin\OnPremisesPermissionsExpanderConfigSamples.zip` file to see more configuration examples.

5.  Start the Permission Expansion Tool and set its configuration, by run a command like the following:

    **Example**

    ```
    C:\Permission_expansion_tool\your_working_folder\bin\Coveo.Connectors.Tools.OnPremisesPermissionExpander.exe ..\Config.json
    ```

#### What's Next

Consider creating a schedule to execute the Permission Expansion Tool recurrently.


