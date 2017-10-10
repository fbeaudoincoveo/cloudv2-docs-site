---
layout: content-2-panel
title: Create an Organization and a Source, and Get Your First Query Results
categories: migrated
---

# Create an Organization and a Source, and Get Your First Query Results

**In this topic:**

-   [Step 1 - Log into the Coveo Cloud V2 Platform for the First Time to Register your Identity](#step-1---log-into-the-coveo-cloud-v2-platform-for-the-first-time-to-register-your-identity)
-   [Step 2 - Get your Coveo Cloud V2 Platform Access Token](#step-2---get-your-coveo-cloud-v2-platform-access-token)
-   [Step 3 - Create a Coveo Cloud V2 Organization](#step-3---create-a-coveo-cloud-v2-organization)
-   [Step 4 - Create an API key](#step-4---create-an-api-key)
-   [Step 5 - Create a Source](#step-5---create-a-source)
-   [Step 6 - Perform a Query](#step-6---perform-a-query)
-   [Step 7 - Delete the Coveo Cloud V2 Organization](#step-7---delete-the-coveo-cloud-v2-organization)

In this short tutorial, you will create a [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization), provision it with a simple web [source](Glossary_37585054.html#Glossary-Source), and perform a few basic [queries](Glossary_37585054.html#Glossary-Query).

## Step 1 - Log into the Coveo Cloud V2 Platform for the First Time to Register your Identity

Assuming you have never used the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform) before, you first need to log in (see [Logging into the Coveo Cloud V2 Platform](Logging_into_the_Coveo_Cloud_V2_Platform)).

## Step 2 - Get your Coveo Cloud V2 Platform Access Token

Now that the Coveo Cloud V2 platform recognizes your identity, you must get an access token with which to authenticate some of the REST API calls you are going to make during this tutorial (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).

## Step 3 - Create a Coveo Cloud V2 Organization

Using the access token you got at [Step 2](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results), create a Coveo Cloud V2 organization (see [Creating a Coveo Cloud V2 Organization](Creating_a_Coveo_Cloud_V2_Organization)).

Note:

> Creating a Coveo Cloud V2 organization is very quick; you should get a successful response within seconds.

Once your organization has been successfully created, you can verify that your access token now has extensive privileges in this new organization (see [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)). In particular, your access token should allow you to view and edit API keys and sources, and execute queries in your organization.

## Step 4 - Create an API key

You will now generate an API key with very limited privileges, which you will use to authenticate your next few calls.

Create an API key using the following instructions (see [Creating an API key](Creating_an_API_Key)):

-   Authenticate the call using the access token you got at [Step 2](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results). 
-   Assign the following privileges to this API key:

    ```
    {
      "type": "EDIT",
      "targetDomain": "SOURCE",
      "owner": "PLATFORM"
    },
    {
      "type": "VIEW",
      "targetDomain": "SOURCE",
      "owner": "PLATFORM"
    },
    {
      "targetDomain": "EXECUTE_QUERY",
      "owner": "SEARCH_API"
    }
    ```

-   Make sure this API key is `enabled`. 
-   Specify adequate values for the following parameters:
    -   `displayName` (e.g., `First Steps Tutorial`) 
    -   `description` (e.g., `Generated on 2017-09-25 for Alice Smith to try creating a source and performing a query.`)

Remember you can only get the API key `value` once, in the successful response body of its creation call.

## Step 5 - Create a Source

A Coveo Cloud V2 organization becomes useful only when it has at least one source of content.

A source can be *secured*, meaning that this source contains permissions associated with each [item](Glossary_37585054.html#Glossary-Item). In this introductory tutorial, however, you will create a *shared* source, meaning that no permissions are associated with items, so that anonymous users can get all source items in their query results.

Using the API key you generated at [Step 4](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results), create a simple shared Web source to index the content of a single public website (see [Creating a Basic Shared Web Source](Creating_a_Basic_Shared_Web_Source)).

To minimize the crawling time, and to make your source quickly searchable, preferably select a website with less than 100 pages for this tutorial. 

Note:

> Creating your very first source should take around 10 minutes, because your Coveo Cloud V2 organization first has to be provisioned.

> Once this process is over, though, creating subsequent sources should only take a few seconds (although crawling and indexing their content can take a while, depending on their respective size).

As soon as your source is created, it starts crawling the target website and processing items in the [Coveo Cloud V2 indexing pipeline](Glossary_37585054.html#Glossary-CoveoCloudV2IndexingPipeline). 

## Step 6 - Perform a Query

When at least one source item is fully processed, you can start querying your [index](Glossary_37585054.html#Glossary-Index) and getting results.

Using the API key you generated at [Step 4](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results), try performing a few simple queries and looking at the results (see [Performing a Simple Query](Performing_a_Simple_Query)).

## Step 7 - Delete the Coveo Cloud V2 Organization

Now that you have completed this tutorial, delete the Coveo Cloud V2 organization you created at [Step 3](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results), unless you want to perform further tests with this organization.

Using the access token you got at [Step 2](Create_an_Organization_and_a_Source,_and_Get_Your_First_Query_Results), delete your Coveo Cloud V2 organization (see [Deleting a Coveo Cloud V2 Organization](Deleting_a_Coveo_Cloud_V2_Organization)).

 
