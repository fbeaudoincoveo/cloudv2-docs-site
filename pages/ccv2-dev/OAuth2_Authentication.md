---
layout: content-2-panel
title: OAuth2 Authentication
categories: migrated
---

# OAuth2 Authentication

[OAuth2](http://oauth.net/2/)is a standard allowing users to delegate access to a system to external applications. This is done through the use of a token which is granted by a user. Tokens can be given specific rights to allow the external application to only use the token for specific purposes. Tokens can also be revoked at any point by the user who created them.

## Obtaining an OAuth2 token

The Coveo implementation of the protocol is compliant with [RFC6749](http://tools.ietf.org/html/rfc6749). We support all four standard grants, but we recommend using the `Authorization Code Grant`. Some grants might not be available to your OAuth2 Client, the list of available grants is given upon [registration of the Client](mailto:support@coveo.com?subject=OAuth2%20Client%20Registration%20Request) (please provide us with the Redirect URI).

The `Authorization Code Grant` starts with the following HTTP request. You need to provide a client ID, the associated redirect URI and the requested scopes as parameters. A specific privilege (or scope) is needed to allow to execute queries. This scope is named executeQuery and should be specified when requesting the token.

**OAuth2 Authorization Endpoint**

```
GET https://cloudplatform.coveo.com/oauth/authorize?response_type=code&client_id=YourClientId&redirect_uri=https://www.example.com/oauth&state=xyz&scope=executeQuery
```

If the user is not authenticated, he will be redirected to the login page. Once the authentication is completed and the user approved the request, the browser will redirect to the specified redirect URI with an authorization code.

**Redirection with an authorization code**

```
302 https://www.example.com/oauth?code=YourAuthorizationCode&state=xyz
```

If the user declined the authorization request, the browser will redirect to the indicated redirect URI with the error code and a description.

**Authorization Denied**

```
302 https://www.example.com/oauth?error=access_denied&error_description=User+denied+access
```

The authorization code can be exchanged for a OAuth2 Token with a POST on the following endpoint :

**OAuth2 Token Endpoint**

```
POST https://cloudplatform.coveo.com/oauth/token HTTP/1.1
Authorization: Basic ICAgLykgLykNCiAgKCBeLl4gKQ0KKGNvVmVvKQ0KQygiKSAoIikNCg==
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=YourAuthorizationCode
&redirect_uri=https://www.example.com/oauth
```

You need to be authenticated as the OAuth2 Client (with Basic Authentication) to convert the authorization code to the OAuth2 Access Token.

**Successful Token Response**

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
    "access_token":"2YotnFZFEjr1zCsicMWpAA",
    "token_type":"example",
    "expires_in":3600,
    "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
    "example_parameter":"example_value"
}
```

 

## Using an OAuth2 token

Once you have obtained an OAuth2 access token, you can use it to execute queries on the Coveo Cloud Search REST API simply by including it in your HTTP request. The token can be specified either in the HTTP headers or via a query string argument.

**The HTTP header method**

That method consists of passing the OAuth2 access token as a standard HTTP header.

**Example: passing an OAuth2 token as an HTTP header**

```
Authorization: Bearer MyAccessToken
```

where MyAccessToken is the OAuth access token.

**The HTTP request parameter method**

That method consists of passing an OAuth2 access token as an HTTP request parameter.

**Example: passing an OAuth2 token as a request parameter**

```
GET https://cloudplatform.coveo.com/rest/search?access_token=thisismytoken&q=test
```

> Using this method is not recommended due to its insecure nature. It should actually be used only in a debugging or development context. Since access tokens appear directly in URLs, they might be recorded and stolen by an attacker. For a safer approach, consider to rather use the HTTP header method.

## OAuth2 Token Scopes and Impersonation

By default, an OAuth2 token issued by the Coveo Cloud platform will only allow executing queries as the user who granted the token. In some cases, it is desirable to provide an external application with a token allowing executing queries as other users. For this purpose the `impersonate` scope can be granted to a token. An application that is given such a token will be able to execute queries as a user it has already authenticated in some way. Of course, tokens with the `impersonate` scope should only be granted to applications that you trust.

Impersonation tokens can be used to directly perform queries as other users, and it's also possible to use them to obtain a so-called [Search Token](Search_Token_Authentication) for an arbitrary user.

### Using an impersonation token to execute queries

When using an impersonation token to directly execute a query, the user that the query should run as is specified via a query string argument named `user`. Here is an example of such a request:

**Example: passing an OAuth2 token as a request parameter**

```
GET https://cloudplatform.coveo.com/rest/search?access_token=thisismytoken&q=test&user=foo@bar.com
```

In this case the token is specified via the query string, but it could also be passed via an HTTP header as described elsewhere.

To use this technique, the entity making the HTTP request must have access to the OAuth2 token. This makes this technique unusable when performing searches directly from the browser, such as when using the [Coveo JavaScript Search Framework](https://developers.coveo.com/display/JsSearch), since the token would have to be included in the HTML code sent to a client. In those cases, it's better to use [Search Tokens](Search_Token_Authentication) as described in the next section.

### Using an impersonation token to create search tokens

Search tokens are a special type of token that only allows to execute queries as a user specified when the token was created. Because of this, they can be safely included in HTML sent to a particular user, allowing JavaScript code to call the Coveo Cloud platform to execute queries.

Search tokens can be obtained by calling the Coveo Cloud platform from trusted server-side code that has access to an impersonation token. This process as well as how the resulting tokens must be used are described in [Search Token Authentication](Search_Token_Authentication).
