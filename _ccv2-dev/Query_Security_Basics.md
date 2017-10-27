---
slug: "106"
layout: content-2-panel
title: Query Security Basics
categories: migrated
toc: ccv2-dev
---

# Query Security Basics

Indexes in the Coveo Cloud V2 platform support item-level security, allowing multiple users of the same index to access only the content they have the right to. Internally, the index removes confidential items from result sets by using information which connectors retrieve during the indexing process. The processes of live indexing and incremental refresh keep this information up-to-date.

Each time a query executes on the Coveo Cloud V2 platform, the platform associates this query to a unique email address. Internally, the platform maps this email address to users from different indexed systems (e.g., a Salesforce user, a Dropbox account, etc.), which makes it possible to search securely across multiple content repositories using a single identity and search query.

## What's Next?

The Coveo Cloud V2 platform provides several different ways to authenticate a user when performing a query (see [Authentication Methods](Authentication_Methods)).
