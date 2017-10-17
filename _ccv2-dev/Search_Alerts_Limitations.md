---
slug: "111"
layout: content-2-panel
title: Search Alerts Limitations
categories: migrated
---

# Search Alerts Limitations

When you enable search alerts in a search page, you should be aware that certain limitations apply concerning search tokens (see [Search Token Authentication](Search_Token_Authentication)).

## Search Alerts Email Notifications and Search Tokens

If you are using search token authentication in a search page, the Search API always sends email notifications to the first user in the array of `userIds` of the token which the user who subscribes to search alerts notifications authenticates with.

This implies that the `name` value of the first entry in the array of `userIds` you specify when creating a search token should always be a valid email address.

This also implies that if you are using a single search token to authenticate more than one user, only the first user in the array of `userIds` of that token actually receives email notifications for search alerts to which any other user who authenticates with that token subscribes.

**Example:**

-   Suppose you generate a search token like this one for a single user whose email address is `john_doe@example.com`:

```
POST /rest/search/token HTTP/1.1
Host: platform.cloud.coveo.com
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "userIds": [
    {
      "name": "anonymous@coveo.com",
      "provider": "Email Security Provider"
    },
    {
      "name": "john_doe@example.com",
      "provider": "Email Security Provider"
    }
  ]
}
```

If the user authenticates with this search token and decides to subscribe to certain search alerts, the Search API will send email notification to `anonymous@coveo.com`, which is probably not the correct address. The user will therefore never receive search alerts email notifications.

-   Now suppose you generate a search token like this one to authenticate four distinct users:

```
POST /rest/search/token HTTP/1.1
Host: platform.cloud.coveo.com
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "userIds": [
    {
      "name": "jane_doe@example.com",
      "provider": "Email Security Provider"
    },
    {
      "name": "john_doe@example.com",
      "provider": "Email Security Provider"
    },
    {
      "name": "bob_smith@example.com",
      "provider": "Email Security Provider"
    },
    {
      "name": "alice_smith@example.com",
      "provider": "Email Security Provider"
    }
  ]
}
```

If user `john_doe@example.com` subscribes to certain search alerts, user `jane_doe@example.com` will actually receive those email notifications.

Moreover, if users `bob_smith@example.com` and `alice_smith@example.com` also subscribe to certain search alerts, `jane_doe@example.com` will receive email notifications for those search alerts as well.

-   If you want search alerts email notifications to work properly while still allowing your search tokens to impersonate the anonymous identity, you should generate a search token like this one for each user:

```
POST /rest/search/token HTTP/1.1
Host: platform.cloud.coveo.com
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "userIds": [
    {
      "name": "john_doe@example.com",
      "provider": "Email Security Provider"
    },
    {
      "name": "anonymous@coveo.com",
      "provider": "Email Security Provider"
    }
  ]
}
```


