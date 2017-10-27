---
slug: "97"
layout: content-2-panel
title: Privileges and API Calls
categories: migrated
---

# Privileges and API Calls

**In this topic:**

-   [Organization, Organization](#organization,-organization)
-   [Group, Organization (targetId: groupId)](#group,-organization-(targetid:-groupid))
-   [Groups, Organization](#groups,-organization)
-   [API Keys, Organization](#api-keys,-organization)
-   [Source, Search Content (targetId: sourceId)](#source,-search-content-(targetid:-sourceid))
-   [Sources, Search Content](#sources,-search-content)
-   [Security Identities, Search Content](#security-identities,-search-content)
-   [Security Identity Providers, Search Content](#security-identity-providers,-search-content)

An administrator of your Coveo Cloud V2 organization can assign privileges to groups and to API keys from the administration console (see [Manage Group: \[GroupName\] - Panel](http://www.coveo.com/go?dest=ccv2ac&context=50) and [API Keys - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=298)).

This topic provides the list of privileges that can be assigned to a group or an API key and the corresponding API calls that can be made with each privilege. 

> All API path are preceded with the Coveo Cloud V2 API host: https://platform.cloud.coveo.com

## Organization, Organization

-   View
    -   GET /rest/organizations/{organizationId}
    -   GET /rest/organizations/{organizationId}/license
    -   GET /rest/organizations/{organizationId}/activities/license
    -   GET /rest/organizations/{organizationId}/activities/organization
    -   GET /rest/organizations/{organizationId}/status
-   Edit
    -   PUT /rest/organizations/{organizationId}/support
    -   DELETE /rest/organizations/{organizationId}
    -   PUT /rest/organizations/{organizationId}

## Group, Organization (targetId: groupId)

-   View
    -   GET /rest/organizations/{organizationId}/groups/{groupId}
    -   GET /rest/organizations/{organizationId}/groups/{groupId}/realms/{realmId}
    -   GET /rest/organizations/{organizationId}/groups/{groupId}/realms
    -   GET /rest/organizations/{organizationId}/groups/{groupId}/invites
    -   GET /rest/organizations/{organizationId}/groups/{groupId}/members/{username}
    -   GET /rest/organizations/{organizationId}/groups/{groupId}/members
-   Edit
    -   DELETE /rest/organizations/{organizationId}/groups/{groupId}
    -   POST /rest/organizations/{organizationId}/groups/{groupId}/realms
    -   DELETE /rest/organizations/{organizationId}/groups/{groupId}/realms|{realmId}
    -   POST /rest/organizations/{organizationId}/groups/{groupId}/invites
    -   DELETE /rest/organizations/{organizationId}/groups/{groupId}/invites/{username}
    -   POST /rest/organizations/{organizationId}/groups/{groupId}/members
    -   DELETE /rest/organizations/{organizationId}/groups/{groupId}/members/{username}
    -   POST /rest/organizations/{organizationId}/groups/{groupId}

## Groups, Organization

-   View
    -   GET /rest/organizations/{organizationId}/groups
    -   GET /rest/organizations/{organizationId}/privileges
    -   GET /rest/organizations/{organizationId}/members/{username}
    -   GET /rest/organizations/{organizationId}/members
-   Edit
    -   POST /rest/organizations/{organizationId}/groups
    -   DELETE /rest/organizations/{organizationId}/members/{username}

## API Keys, Organization

-   View
    -   GET /rest/organizations/{organizationId}/apikeys
    -   GET /rest/organizations/{organizationId}/apikeys/{apiKeyId}
    -   GET /rest/organizations/{organizationId}/activities/apikey
    -   GET /rest/organizations/{organizationId}/privileges/apikeys
-   Edit
    -   POST /rest/organizations/{organizationId}/apikeys
    -   DELETE /rest/organizations/{organizationId}/apikeys/{apiKeyId}
    -   PUT /rest/organizations/{organizationId}/apikeys/{apiKeyId}
    -   PUT /rest/organizations/{organizationId}/apikeys/{apiKeyId}/activate
    -   PUT /rest/organizations/{organizationId}/apikeys/{apiKeyId}/disable

## Source, Search Content (targetId: sourceId)

-   View
    -   GET /rest/organizations/{organizationId}/sources/{sourceId}
    -   GET /rest/organizations/{organizationId}/sources/{sourceId}/configuration/salesforce/objects/{objectName}/fields
    -   GET /rest/organizations/{organizationId}/sources/{sourceId}/raw
    -   GET /rest/organizations/{organizationId}/sources/{sourceId}/schedules
-   Edit
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/applyChanges
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/schedules
    -   DELETE /rest/organizations/{organizationId}/sources/{sourceId}
    -   DELETE /rest/organizations/{organizationId}/sources/{sourceId}/schedules/{scheduleId}
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/disable
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/enable
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/fullRefresh
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/incrementalRefresh
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/pauseRefresh
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/rebuild
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/resumeRefresh
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/startRefresh
    -   POST /rest/organizations/{organizationId}/sources/{sourceId}/stopRefresh
    -   PUT /rest/organizations/{organizationId}/sources/{sourceId}/raw
    -   PUT /rest/organizations/{organizationId}/sources/{sourceId}
    -   PUT /rest/organizations/{organizationId}/sources/{sourceId}/schedules/{scheduleId}
    -   DELETE /rest/organizations/{organizationId}/activities/sources/{sourceId}/{activityId}
    -   POST /rest/organizations/{organizationId}/activities/sources/{sourceId}/{activityId}/cancel
    -   POST /rest/organizations/{organizationId}/activities/sources/{sourceId}/{activityId}/pause
    -   POST /rest/organizations/{organizationId}/activities/sources/{sourceId}/{activityId}/resume
    -   POST /rest/organizations/{organizationId}/activities/sources/{sourceId}/pushapi/{activityOperation}

## Sources, Search Content

-   View
    -   GET /rest/organizations/{organizationId}/sources
    -   GET /rest/organizations/{organizationId}/sources/fields
    -   GET /rest/organizations/{organizationId}/sources/fields/{fieldId}
    -   GET /rest/organizations/{organizationId}/sources/page/fields
    -   GET /rest/organizations/{organizationId}/indexes/fields
    -   GET /rest/organizations/{organizationId}/indexes/fields/{fieldId}
    -   GET /rest/organizations/{organizationId}/indexes/page/fields
    -   GET /rest/organizations/{organizationId}/activities/fields
    -   GET /rest/organizations/{organizationId}/activities/sources/{sourceId}
-   Edit
    -   POST /rest/organizations/{organizationId}/indexes/fields
    -   POST /rest/organizations/{organizationId}/indexes/fields/batch/create
    -   DELETE /rest/organizations/{organizationId}/indexes/fields/{fieldId}
    -   DELETE /rest/organizations/{organizationId}/indexes/fields/batch/delete
    -   PUT /rest/organizations/{organizationId}/indexes/fields/{fieldId}
    -   PUT /rest/organizations/{organizationId}/indexes/fields/batch/update
    -   POST /rest/organizations/{organizationId}/sources
    -   POST /rest/organizations/{organizationId}/sources/raw
    -   POST /rest/organizations/{organizationId}/sources/fields
    -   POST /rest/organizations/{organizationId}/sources/fields/batch/create
    -   DELETE /rest/organizations/{organizationId}/sources/fields/{fieldId}
    -   DELETE /rest/organizations/{organizationId}/sources/fields/batch/delete
    -   PUT /rest/organizations/{organizationId}/sources/fields/{fieldId}
    -   PUT /rest/organizations/{organizationId}/sources/fields/batch/update

## Security Identities, Search Content

-   View
    -   GET /rest/organizations/{organizationId}/indexes/{indexId}/documents/{documentId}/permissions/effective
    -   GET /rest/organizations/{organizationId}/indexes/{indexId}/documents/{documentId}/permissions
    -   GET /rest/organizations/{organizationId}/activities/permissions
    -   GET /rest/organizations/{organizationId}/securitycache/schedule
    -   GET /rest/organizations/{organizationId}/securitycache/status
-   Edit
    -   POST /rest/organizations/{organizationId}/securitycache/refresh
    -   POST /rest/organizations/{organizationId}/securitycache/refresh/entity
    -   PUT /rest/organizations/{organizationId}/securitycache/schedule

## Security Identity Providers, Search Content

-   View
    -   GET /rest/organizations/{organizationId}/securityproviders
    -   GET /rest/organizations/{organizationId}/securityproviders/{securityProviderName}
    -   GET /rest/organizations/{organizationId}/securityproviders/{securityProviderName}/raw
    -   GET /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}
    -   GET /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}/raw
    -   GET /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders
    -   GET /rest/organizations/{organizationId}/clusters/{organizationClusterId}/sources/{sourceId}/securityproviders/
-   Edit
    -   POST /rest/organizations/{organizationId}/securityproviders/{securityProviderName}
    -   PUT /rest/organizations/{organizationId}/securityproviders/{securityProviderName}/raw
    -   DELETE /rest/organizations/{organizationId}/securityproviders/{securityProviderName}/{referenceType}/{referenceId}
    -   DELETE /rest/organizations/{organizationId}/securityproviders/{securityProviderName}
    -   PUT /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}
    -   PUT /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}/raw
    -   DELETE /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}
    -   DELETE /rest/organizations/{organizationId}/clusters/{organizationClusterId}/securityproviders/{securityProviderName}/{referenceType}/{referenceId}
    -   POST /rest/organizations/{organizationId}/securitycache/{providerName}/refresh

