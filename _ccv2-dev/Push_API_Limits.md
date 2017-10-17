---
slug: "99"
layout: content-2-panel
title: Push API Limits
categories: migrated
---

# Push API Limits

The Push API enforces certain request size and call frequency limits.

## Request Size Limits

> Be aware that these limits could change at any time without prior notice.

You will typically get a `413 Request Entity Too Large` response if:

-   Your total request size exceeds 256 megabytes when pushing a large file container (see [Pushing Large Items to a Source](Pushing_Large_Items_to_a_Source) and [Batch Pushing Encrypted Files and Permissions to a Source](Batch_Pushing_Encrypted_Files_and_Permissions_to_a_Source)).
-   Your total request size exceeds 6 megabytes when pushing a single compressed or uncompressed item (see Pushing Items to a Source).

## Recommended Maximum Number of Items/Identities per Hour

> Be aware that these recommendations could change at any time without prior notice.

As a guideline, you should avoid adding, updating, and/or deleting more than one million items/identities per hour. Otherwise, you risk getting `429 TOO_MANY_REQUESTS` responses.

> This does not imply that you should ever make one million push API *calls* per hour.

> Typically, you should start by making a few test calls to understand how the Push API works. The best practice is to use the "single" push operations ([Add or update single item](https://platform.cloud.coveo.com/docs?api=PushApi#!/document/put_organizations_organizationId_sources_sourceId_documents), [Delete single item](https://platform.cloud.coveo.com/docs?api=PushApi#!/document/delete_organizations_organizationId_sources_sourceId_documents), [Add or update single identity](https://platform.cloud.coveo.com/docs?api=PushApi#!/identity/put_organizations_organizationId_providers_providerId_permissions), etc.) when making those tests.

> Once you feel ready, you should start actually adding content to your Coveo Cloud V2 organization index by using the "batch" push operations ([Add, update, and/or delete batch of items](https://platform.cloud.coveo.com/docs?api=PushApi#!/document/put_organizations_organizationId_sources_sourceId_documents_batch), [Add, update, and/or delete batch of identities](https://platform.cloud.coveo.com/docs?api=PushApi#!/identity/put_organizations_organizationId_providers_providerId_permissions_batch)). These operations allow you to push large number of items and/or identities, while keeping your number of Push API calls per hour relatively low.


