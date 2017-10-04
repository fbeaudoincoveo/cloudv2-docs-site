---
layout: content-2-panel
title: JavaScript Push API Client Example
categories: migrated
---

# JavaScript Push API Client Example

You can take advantage of the Push API to send items, such as direct messages, to a Coveo Cloud V2 push type source.

The following JavaScript sample uses a real time messaging client to push a message from a public Slack channel to the Push API (see [Node Library for the Slack APIs](https://www.npmjs.com/package/@slack/client)).

> More details about the JavaScript Push API client usage are available from <https://github.com/coveo/coveo-slack-pushapi>.

```
var RtmClient = require('@slack/client').RtmClient;
var RTM_EVENTS = require('@slack/client').RTM_EVENTS;
var CLIENT_EVENTS = require('@slack/client').CLIENT_EVENTS;
var MemoryDataStore = require('@slack/client').MemoryDataStore;
var request = require('request');

module.exports = PushClient;

 
function PushClient(slacktoken, organizationId, sourceId, pushtoken) {
    this.slacktoken = slacktoken || ''; // Go to https://api.slack.com/docs/oauth-test-tokens to get your token
    this.organizationId = organizationId || '';
    this.sourceId = sourceId || '';
    this.pushtoken = pushtoken || ''; // Your API key or access_token from the administration console cookie
    this.init();
    this.bindEvents();
}

// Initialize the RTM client and a memory data store
PushClient.prototype.init = function() {
    this.rtm = new RtmClient(this.slacktoken, {
        logLevel: 'error',
        dataStore: new MemoryDataStore()
    });
}

PushClient.prototype.start = function() {
    this.rtm.start();
}

PushClient.prototype.handleAuthenticated = function(rtmStartData) {
    this.rtmStartData = rtmStartData;
    this.team = rtmStartData.team;
}

PushClient.prototype.handleNewMessage = function(message) {
    var _this = this;

    // Build the BODY of the message
    var document = _this.buildMessageDocument(message);

    // Logging
    console.log(`Sending message from ${_this.rtm.dataStore.getUserById(message.user).name} 
                in channel ${_this.rtm.dataStore.getChannelGroupOrDMById(message.channel).name} 
                @ ${message.ts}`);

    // Push the message to the Push API
    _this.pushDocument(JSON.stringify(document), document.documentId);
}

PushClient.prototype.pushDocument = function(documentBody, documentId) {
    var _this = this;

    var server = 'push.cloud.coveo.com'
    var APIversion = 'v1'

    // Push the message to your source
    request({
        url: `https://${server}/${APIversion}/organizations/${_this.organizationId}/sources/${_this.sourceId}/documents`,
        qs: { documentId: documentId },
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
            'Authorization': 'Bearer ' + _this.pushtoken
        },
        body: documentBody
    }, function(error, response, body) {
        if (error) { // Handle errors here, for example you could retry X number of times
            console.error(error);
        } else if (response.statusCode == 202) { // Success
            console.log('Success!');
        }
    });
}

PushClient.prototype.buildMessageDocument = function(message) {
    var _this = this;

    // Get the channel name of the message
    var channel = _this.rtm.dataStore.getChannelGroupOrDMById(message.channel).name;
    channel = (channel === 'undefined') ? 'Direct Message' : channel; // Direct messages have a channel name = 'undefined'
    var timeStr = message.ts.replace('.', '');

    // Build the documentId
    var documentId = `https://${_this.team.name}.slack.com/archives/${channel}/p${timeStr}`; // Your documentId must be in this URI format

    var user = _this.rtm.dataStore.getUserById(message.user).name || '';

    var body = {
        documentId: documentId,
        message: message.text,
        Data: message.text,
        team: _this.team.name,
        channel: channel,
        type: message.type,
        user: user,
        timestamp: message.ts
    }

    return body;
}

PushClient.prototype.bindEvents = function() {
    var _this = this;
    this.rtm.on(CLIENT_EVENTS.RTM.AUTHENTICATED, function onAuthenticated(rtmStartData) { _this.handleAuthenticated(rtmStartData); });
    this.rtm.on(RTM_EVENTS.MESSAGE, function onRtmMessage(message) { _this.handleNewMessage(message); });
    this.rtm.on(RTM_EVENTS.REACTION_ADDED, function onRtmReactionAdded(reaction) { _this.handleReaction(reaction); });
    this.rtm.on(RTM_EVENTS.REACTION_REMOVED, function onRtmReactionRemoved(reaction) { _this.handleReactionRemoved(reaction); });
}
```


