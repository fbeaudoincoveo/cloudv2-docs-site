---
layout: content-2-panel
title: Batch Pushing Encrypted Files and Permissions to a Source
categories: migrated
---

# Batch Pushing Encrypted Files and Permissions to a Source

 

In this topic: /\*\*/ Batch Pushing Identities to an Identity Provider This topic describes how to efficiently and securely push your system items and permissions into a Coveo Cloud V2 push type source using the Push API batch process.

It is recommended that you use this method when pushing a large number of items, especially when they contain personal information. Before your compressed or uncompressed content is pushed to your source, it is uploaded to a properly encrypted file hosted in Amazon S3, whose infrastructure allows to securely index your data in your Coveo Cloud V2 organization. Once your items are indexed, the S3 file is deleted.

1.  If not already done, create a push type source and get an API key (see Add/Edit a Push Source - Panel).
2.  Get all the required parameters (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).
    1.  Organization and source IDs
    2.  File ID and upload URI

3.  Upload content to the file in Amazon S3 via Postman.
    1.  Launch Postman.

    2.  Select PUT and enter the `uploadUri` into the **request URL** box as shown in the following example:

        ```
        PUT https://s3.amazonaws.com/coveo-nprod-customerdata/proda/blobstore/mycoveoorg/60e285b1-58ec-5625-c5c4-53cd2434c19f?x-amz-security-token=FQoDYXdzEKX%2Fici...
        ```

        > This call is not available from <https://platform.cloud.coveo.com/docs>.

    3.  Your call must include the following headers:

        | Key                            | Value                      |
        |--------------------------------|----------------------------|
        | `Content-Type`                 | `application/octet-stream` |
        | `x-amz-server-side-encryption` | `AES256`                   |

    4.  Enter a JSON in a format similar to the following example:

        ```
        {
          "AddOrUpdate": [
            {
              "DocumentId": "https://en.wikipedia.org/wiki/Advanced_Encryption_Standard",
              "title": "Advanced Encryption Standard",
              "Data": "The Advanced Encryption Standard (AES)..."
            },
            {
              "DocumentId": "https://en.wikipedia.org/wiki/Data_Encryption_Standard",
              "title": "Data Encryption Standard",
              "Data": "The Data Encryption Standard..."
            }
          ],
          "Delete": [
            {
              "DocumentId": "https://en.wikipedia.org/wiki/Cryptography,
              "deleteChildren": true"
            }
          ]
        }
        ```

        where you can add, update, and delete items (and if applicable their attachments). The `documentId` must be a unique URI.
        Replace the `Data` reserved key by the `CompressedBinaryDataFileId` reserved key when indexing compressed content. Your JSON data must be compressed using one of the supported compression types (Deflate, GZip, LZMA, Uncompressed, or ZLib).

    5.  Send your request and ensure that it returns a `200 OK` response code.

4.  Push the items from Amazon S3 to your source.
    1.  Use the following call:

        ```
        PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents/batch?fileId=<fileId>&orderingId=<orderingId>
        ```

        where you replace `<organizationId>`, `<sourceId>` and `<fileId>` by their real values. The `orderingId` is required when you want to delete old items.

    2.  Include the following headers:

        | Key             | Value                         |
        |-----------------|-------------------------------|
        | `Authorization` | `Bearer valid_API_key value>` |
        | `Content-Type`  | `application/json`            |

    3.  Send your request and ensure it returns a `202 Success` response code.

5.  In the administration console, validate that the files are pushed to your source.

    -   In the **Sources** page, within a few minutes you can see the number of processed items in the Status column, or watch the \[Nb\] items value change in the Content column (see Understanding Push API Processing Delay). 
    -   In the navigation panel, under Search Content, select Content Browser:

    1.  1.  In the Source facet, select your push type source.
        2.  In the search results, look for the addition or the update of pushed items, which can occur minutes after they were reported to be in the source.

    > If you do not see your content in the administration console **Sources** page, your request(s) may contain invalid data (see <https://www.getpostman.com/docs/requests>).

6.  Validate that your content is properly indexed by searching for keywords or phrases they contain and looking at their Quick View.

## Batch Pushing Identities to an Identity Provider

Coveo Cloud V2 secured sources can contain multiple security identities with allowed and denied permissions on each item to ensure that your content is viewable only by the allowed members of your organization (see Source Permission Types).

1.  If not already done, create an identity provider that can be provisioned using the Push API (see [Creating an Identity Provider for a Secured Source](https://developers.coveo.com/x/MoodAg)).
2.  Upload your item permissions to the file hosted in Amazon S3.
    1.  Select PUT and enter the uploadUri.

        ```
        PUT <uploadUri>
        ```

    2.  Your call must include the following headers:

        | Key                            | Value                      |
        |--------------------------------|----------------------------|
        | `Content-Type`                 | `application/octet-stream` |
        | `x-amz-server-side-encryption` | `AES256`                   |

    3.  Enter a JSON like the following:

        ```
        {
            "Members": [
                {
                    "Identity": {
                        "Name": "Cryptographers",
                        "Type": "Group",
                        "AdditionalInfo": {}
                    },
                    "Members": [
                        {
                            "Name": "Cryptographer1",
                            "Type": "User",
                            "AdditionalInfo": {}
                        },
                        {
                            "Name": "Cryptographer2",
                            "Type": "User",
                            "AdditionalInfo": {}
                        }
                    ],
                    "WellKnowns": [
                        {
                            "Name": "WellKnownCryptographers",
                            "Type": "Group",
                            "AdditionalInfo": {}
                        }
                    ]
                }
            ],
            "Mappings": [
                {
                    "Identity": {
                        "Name": "Cryptographers",
                        "Type": "Group",
                        "AdditionalInfo": {}
                    },
                    "Mappings": [
                        {
                            "Name": "Cryptographers",
                            "Type": "Group",
                            "AdditionalInfo": {},
                            "Provider": "Email Security Provider"
                        }
                    ],
                    "WellKnowns": [
                        {
                            "Name": "cryptographer1@mycompany.com",
                            "Type": "User",
                            "AdditionalInfo": {}
                        },
                        {
                            "Name": "cryptographer1@mycompany.com",
                            "Type": "User",
                            "AdditionalInfo": {}
                        }
                    ]
                }
            ],
            "Deleted": [
                {
                    "Identity": {
                        "Name": "Cryptographer3",
                        "Type": "User",
                        "AdditionalInfo": {}
                    }
                }
            ]
        }
        ```

    4.  Send your request.

3.  Push your permissions to your identity provider.

    1.  Use the following API call:

        ```
        PUT http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions/batch?fileId=<fileId>&orderingId=<orderingId>
        ```

        where you replace `<organizationId>`, `<providerId>` and `<fileId>` by their real values. The `orderingId` is required when you want to delete old identities (see [Pushing Identities to an Identity Provider](https://developers.coveo.com/x/JoodAg)).

    2.  Include the following headers:

        | Key             | Value                         |
        |-----------------|-------------------------------|
        | `Authorization` | `Bearer valid_API_key value>` |
        | `Content-Type`  | `application/json`            |

    3.  Send your request.

    4.  In the administration console **Security Identities** page, validate that your security identities are pushed to your identity provider, monitoring the number in the **Identities** column increase or decrease.

 

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [image2016-6-3 8:56:8.png](attachments/35489765/35455210.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2016-6-3 8:56:53.png](attachments/35489765/35455211.png) (image/png)

