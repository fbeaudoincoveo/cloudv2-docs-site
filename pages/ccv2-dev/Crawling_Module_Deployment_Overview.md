---
layout: content-2-panel
title: Crawling Module Deployment Overview
categories: migrated
---

# Crawling Module Deployment Overview

Note:

> The Coveo Cloud V2 Crawling Module is currently in an alpha version and must be deployed with the Coveo Support assistance.

You need to deploy one Crawling Module instance for each repository that you want to index. 

The steps required to deploy a Crawling Module instance are:

1.  Ensure that your environment meets the requirements (see Crawling Module Requirements).
2.  Create a secured push type source and get an API key (see Creating a Push Type Source).
3.  Ensure that your API key has the right privileges.
    In the administration console API Access page, select the View check boxes for the following privileges:
    1.  Security identities
    2.  Security identity providers
    3.  Sources

4.  Install the Crawling Module on your server (see Installing the Crawling Module). 
5.  Configure the Crawling Module (see Crawling Module Configuration).
6.  Before indexing item permissions, and if applicable, understand the steps required to resolve them (see [Understanding How On-Premises Item Permissions are Resolved](https://developers.coveo.com/x/HookAg)).

    1.  Create an Expanded Security Identity Provider for your source (see Creating an Identity Provider for a Secured Push Type Source).

    2.  Configure the Permission Expansion Tool (Configuring a Permission Expansion Tool for a Secured Source).

         

7.  Schedule Crawling Module recurrent tasks (see [Running a Crawling Module instance](https://developers.coveo.com/x/54YkAg)).

