---
slug: "125"
layout: content-2-panel
title: Valid Privilege owner, targetDomain, and type Combinations
categories: migrated
---

# Valid Privilege owner, targetDomain, and type Combinations

In the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform), privileges determine who can do what in the platform (see [Privileges](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=300)). A privilege is minimally represented by a valid combination of an `owner` value (either `USAGE_ANALYTICS`, `PLATFORM`, or `SEARCH_API`), and a `targetDomain` value (`REPORTS`, `SOURCE`, `EXECUTE_QUERY`, etc). Most privileges must also have a `type` value (either `VIEW` or `EDIT`).

The following table lists the `owner`, `targetDomain`, and `type` value combinations which are recognized as [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization) privileges, and their corresponding display values in the [Coveo Cloud V2 administration console](Glossary_37585054.html#Glossary-CoveoCloudV2AdministrationConsole).

| `owner`           | `targetDomain`                | `type` values allowed | Administration console Service | Administration console Name    |
|-------------------|-------------------------------|-----------------------|--------------------------------|--------------------------------|
| `USAGE_ANALYTICS` | `ADMINISTRATE`                |                       | Analytics                      | Administrate                   |
| `USAGE_ANALYTICS` | `ANALYTICS_DATA`              | `VIEW`, `EDIT`        | Analytics                      | Analytics data                 |
| `USAGE_ANALYTICS` | `EXPORTS`                     | `VIEW`, `EDIT`        | Analytics                      | Data exports                   |
| `USAGE_ANALYTICS` | `CUSTOM_DIMENSIONS`           | `VIEW`, `EDIT`        | Analytics                      | Dimensions                     |
| `USAGE_ANALYTICS` | `IMPERSONATE`                 |                       | Analytics                      | Impersonate                    |
| `USAGE_ANALYTICS` | `NAMED_FILTERS`               | `VIEW`, `EDIT`        | Analytics                      | Named filters                  |
| `USAGE_ANALYTICS` | `PERMISSION_FILTERS`          | `VIEW`, `EDIT`        | Analytics                      | Permission filters             |
| `USAGE_ANALYTICS` | `REPORTS`                     | `VIEW`, `EDIT`        | Analytics                      | Reports                        |
| `USAGE_ANALYTICS` | `QUERY_SUGGEST`               |                       | Analytics                      | Suggest queries                |
| `USAGE_ANALYTICS` | `VIEW_ALL_REPORTS`            |                       | Analytics                      | View all reports               |
| `PLATFORM`        | `INDEXING_PIPELINE_EXTENSION` | `VIEW`, `EDIT`        | Content                        | Extensions                     |
| `PLATFORM`        | `SECURITY_CACHE`              | `VIEW`, `EDIT`        | Content                        | Security identities            |
| `PLATFORM`        | `SECURITY_PROVIDER`           | `VIEW`, `EDIT`        | Content                        | Security identity providers    |
| `PLATFORM`        | `SOURCE`                      | `VIEW`, `EDIT`        | Content                        | Sources                        |
| `PLATFORM`        | `API_KEY`                     | `VIEW`, `EDIT`        | Organization                   | API keys                       |
| `PLATFORM`        | `ACTIVITIES`                  | `VIEW`, `EDIT`        | Organization                   | Activities                     |
| `PLATFORM`        | `GROUP`                       | `VIEW`, `EDIT`        | Organization                   | Groups                         |
| `PLATFORM`        | `ON_PREMISE_ADMINISTRATION`   | `VIEW`, `EDIT`        | Organiation                    | On-premises administration     |
| `PLATFORM`        | `ORGANIZATION`                | `VIEW`, `EDIT`        | Organization                   | Organization                   |
| `PLATFORM`        | `SAML_IDENTITY_PROVIDER`      | `VIEW`, `EDIT`        | Organization                   | Saml identity provider         |
| `PLATFORM`        | `SUBSCRIPTION`                | `VIEW`, `EDIT`        | Organization                   | Subscriptions                  |
| `SEARCH_API`      | `EXECUTE_QUERY`               |                       | Search                         | Execute queries                |
| `SEARCH_API`      | `IMPERSONATE`                 |                       | Search                         | Impersonate                    |
| `SEARCH_API`      | `AUTHENTICATION_EDITOR`       |                       | Search                         | Modify authentication provider |
| `SEARCH_API`      | `QUERY_PIPELINE`              | `VIEW`, `EDIT`        | Search                         | Query pipelines                |
| `SEARCH_API`      | `SALESFORCE_AUTHENTICATION`   | `VIEW`, `EDIT`        | Search                         | Salesforce index configuration |
| `SEARCH_API`      | `SEARCH_PAGES`                | `VIEW`, `EDIT`        | Search                         | Search pages                   |
| `SEARCH_API`      | `VIEW_ALL_CONTENT`            |                       | Search                         | View all content               |

Note:

> An API key cannot have any of the privileges whose `targetDomain` is `API_KEY` (i.e., API keys cannot view or edit other API keys).


