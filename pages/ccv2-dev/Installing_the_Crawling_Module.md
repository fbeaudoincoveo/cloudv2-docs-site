---
layout: content-2-panel
title: Installing the Crawling Module
categories: migrated
---

# Installing the Crawling Module

Note:

> The Coveo Cloud V2 Crawling Module is currently in an alpha version and must be installed with the Coveo Support assistance.

 

The Coveo Crawling Module package includes templates for all available crawler types.

You need to install one Crawling Module for each Coveo Cloud organization source to which you want to push content. You can however easily install other Crawling Module instances by copying and pasting its working folder, and then changing the port and other appropriate parameters in the configuration files. 

1.  Get the Crawling Module package.

    Note:

    > Currently, the Crawling Module package is in an alpha version so you need to contact your client executive to get the ZIP file.

     

2.  Before installing the provided package, ensure that your environment meets the requirements (see Crawling Module Requirements).
3.  Install the package:
    1.  Create a Crawling Module instance folder (example:` C:\Crawling_module\your_working_folder`).
        When running multiple Crawling Module instances, create a different folder for each of them (example: `C:\Crawling_module\File_server`).
    2.  In `your_working_folder`, unzip the `CoveoConnectorsComponentPackage.zip` file.
    3.  In `your_working_folder\bin\`, unzip the `your_working_folder\bin\CoveoPushApi.zip` file.
    4.  When your repository to index is a database and the targeted database driver is in 32-bit architecture, in `your_working_folder\bin\`, unzip the `your_working_folder\bin\Win32ConnectorUtilities.zip` file.
        The `Win``32` folder appears.
    5.  Install Python dependencies.
        1.  Run CMD as an administrator.
        2.  Execute the following command:

            ```
            pip install pycoveo-cdf-1.0.21.zip
            ```

            > The `pycoveo-cdf` version number can be different in the `CoveoPushApi.zip` file.

            **Example**

            ```
            C:\Python27\Scripts\pip.exe install C:\Crawling_module\working_folder\bin\pycoveo-cdf-1.0.21.zip
            ```

    6.  In `your_working_folder`, unzip `your_working_folder\instances\<your_connector>Template.zip` where `<your_connector>` corresponds to the repository type you want to index. 

        **Example:**

        When you want to a Crawling Module for a database, unzip the following file in `your_working_folder:`

        `your_working_folder\instances\DatabaseInstanceTemplate.zip`

    7.  Copy `your_working_folder\bin\Config_template.json` in `your_working_folder`, and rename it `config.json`.
    8.  Copy `your_working_folder\Crawler.json.template` in `your_working_folder`, and rename it `crawler.json`.

 
