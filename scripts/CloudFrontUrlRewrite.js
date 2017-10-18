'use strict';

/* Lambda sample originally from:
 *  - https://linuxacademy.com/howtoguides/posts/show/topic/19955-url-rewriting-in-aws-cloudfront
 *  - http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirect-based-on-country
 *
 */

/* This is an origin request function */
exports.handler = (event, context, callback) => {
    // The request we want to re-map
    const request = event.Records[0].cf.request;
    // Get the original 'uri' property to overwrite
    const originalUri = request.uri;

    // Keep only the ID initial part together with the search query parameters and hash
    // Example: /4/api-explorer/Coveo-Cloud-V2-APIs?extUrl=1&test=123#somehash  = > /4/?extUrl=1&test=123#somehash
    request.uri = originalUri.replace(/^(\/[0-9]*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$/,"$1$3");

    // quit the lambda and let the request chain continue
    callback( null, request );
};
