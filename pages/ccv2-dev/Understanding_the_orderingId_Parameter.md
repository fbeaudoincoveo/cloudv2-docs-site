---
layout: content-2-panel
title: Understanding the orderingId Parameter
categories: migrated
---

# Understanding the orderingId Parameter

Understanding how the `orderingId` parameter works is especially important when you push content into a Coveo Cloud V2 organization index using the crawling module.

## Explanation

All Push API operations, except the [Get a large file container](https://platform.cloud.coveo.com/docs?api=PushApi#!/file/post_organizations_organizationId_files) and [Set the source status](https://platform.cloud.coveo.com/docs?api=PushApi#!/source/post_organizations_organizationId_sources_sourceId_status) operations, have a numeric `orderingId` value. This value indicates the "age" of the operation: the lower the `orderingId` value is, the "older" the Push API considers the operation to be.

**Example:**

A Push API operation whose `orderingId` value is 1506700606240 predates an operation whose orderingId value is 1506700606241.

In theory, you could manually set the `orderingId` of the Push API operations you perform to any arbitrary unsigned long integer value. However, if you decide to provide your own `orderingId` values, you should increase the value you assign to the `orderingId` parameter each time you perform a new Push API operation. In essence, any given Push API operation should have a higher `orderingId` than that of its immediate predecessor.

**Example:**

You perform an operation to push an item. You manually assign `1` as the `orderingId` of this operation. Immediately after, you perform an operation to delete the item you just pushed. You manually assign `2` as the `orderingId` of the delete operation.

If you do not manually specify a value for the `orderingId` parameter when making a Push API call, the Push API automatically sets the `orderingId` value to the current number of milliseconds since UNIX epoch.

**Example:**

You perform an operation to push an item. You do not manually specify an `orderingId` for this operation, so the Push API automatically sets its value to the current number of milliseconds since UNIX epoch (e.g., `1506702742423`). Later, you perform an operation to delete the item you just pushed. You also avoid manually specifying an `orderingId` for this delete operation, so the Push API uses the new current UNIX epoch time (e.g., `1506702797449`).

Things get more complex when you start using the crawling module to push content, because the crawling module automatically sets the `orderingId` value of a Push API operation to the current number of nanoseconds since 1440 (which is a much higher number than the number of milliseconds since UNIX epoch).

**Example:**

You use the crawling module to push an item. The crawling module automatically sets the `orderingId` of this operation to a very high number (e.g., `19457712023373612345`). Later, you perform an operation to delete the item the crawling module pushed. You do not manually specify an `orderingId` value, so the Push API uses the current UNIX epoch time (e.g., `1506703394`). However, this value is much lower than the orderingId which was previously assigned to the push operation by the crawling module. Consequently, the Push API considers the delete operation to predate the push operation, which makes no sense. The delete operation fails.

In this case, if you want the delete operation work, you need to manually specify an orderingId value which is higher than 19457712023373612345.

> When the Coveo for Sitecore implementation performs a Push API operation, it automatically sets the `orderingId` value of this operation to the current .NET Framework ticks (e.g., `636423001940000000`**)**.


