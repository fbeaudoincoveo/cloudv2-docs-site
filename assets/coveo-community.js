/* Code from the coveo-community-unified-navigation repo */

$(window).ready(function(){
    trackEventsGa();
    //trigger mobile menu
    $(".currentSiteName").click(function(){
        $("+ nav",this).slideToggle();
        $(">span i",this).toggleClass("up");
    });
    $(".upHeader nav ul.menu a,.upHeader .externalbox a").click(function(e){
        if (isMobile()){
            e.preventDefault();
            $(".upHeader nav").slideUp();
            window.open($(this).attr("href"),"_blank");
        }
    });
    //open submenu in connected mode
    $("a.connected").click(function(e){
        e.preventDefault();
        $("+ ul",this).slideToggle();
    });
});

function trackEventsGa(){
    //tracking for analytics.js
    //if ga.js use _gaq.push(['_trackEvent', 'button3', 'clicked']) template
    $("#jsSupport").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Support');});
    $("#jsProductDocs").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Product docs');});
    $("#jsDevDocs").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Dev docs');});
    $("#jsAnswers").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Answers');});
    $("#jsTraining").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Training');});
    $("#jsCloudAdminV1").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Cloud Admin V1');});
    $("#jsCloudAdminV2").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Cloud Admin V2');});
    $("#jsTechBlog").click(function(){ ga('send', 'event', 'TopMenus', 'click', 'Tech Blog');});
}

//Mobile detection
function isMobile(){
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        return true;
    }
}

// Set the Coveo Cloud Organization search and analytics tokens
var siteOrigin= 'CoveoDocs'; // Telling search.coveo.com where the search request comes from
var SuggestionScope = '@source==CoveoProductDocsStagingOnS3'; //Search Box suggestion filter ex: @syssource=("ohclouden")
var searchToken = 'xx1b26c04d-9505-4a61-bab2-ff29d6d4efc1'; //API Key allowing to query
var uaToken = searchToken; // API Key for allowing to push Usage analytics events
var hostname = window.location.hostname; //To manage dev/staging/prod environment
var TechDocSearchPage = 'https://search.coveo.com/techdocccv2.html';
if (hostname === "d3in5cp0cx0iu6.cloudfront.net" | hostname === "coveo-products-docs.s3-website-us-east-1.amazonaws.com/" || hostname === "127.0.0.1" | hostname === "localhost") {
    // Use the "Coveo - Documentation test" Cloud V2 production org
    searchToken = 'xx37d9ea69-1669-45da-b615-3ee13f463010';
    uaToken = searchToken;
    TechDocSearchPage = 'https://platform.cloud.coveo.com/pages/coveodocumentationtest/CoveoProductDocsStagingOnS3';
}

$(function(){
    // Define the Coveo endpoint for the search box
    Coveo.SearchEndpoint.endpoints["default"] = new Coveo.SearchEndpoint({
        restUri: 'https://platform.cloud.coveo.com/rest/search',
        accessToken: searchToken
    });

    // Adding the site origin to the search state
    $("#searchBox").on("afterInitialization", function(){
        $("#searchBox").coveo('state', 'site', siteOrigin);
    });
    // Initializing the search box
    $('#searchBox').coveo('initSearchbox', TechDocSearchPage, {
        FieldSuggestions: {
            omniboxSuggestionOptions: {
                onSelect: function (valueSelected, populateOmniBoxEventArgs) {
                    populateOmniBoxEventArgs.closeOmnibox();
                    Coveo.SearchEndpoint.endpoints["default"]
                        .search({
                            q: '@docstitle=="' + valueSelected + '"',
                            aq: SuggestionScope
                        })
                        .done(function (results) {
                            var foundResult = Coveo._.find(results.results, function(result){
                                return valueSelected == result.raw.systitle && !result.ClickUri.includes('/ac8/');
                            });
                            if(foundResult){
                                // logCustomEvent('pageNav', 'omniboxTitleSuggestion', uaToken, foundResult.Title, foundResult.clickUri);
                                //console.log('Navigation type, label, target: ' + 'omniboxTitleSuggestion' + ' | ' + foundResult.Title + ' | ' + foundResult.clickUri);
                                window.location = foundResult.clickUri;
                            } else {
                                logger.warn("Selected suggested result," + valueSelected + " , not found.");
                            }
                        })
                },
                queryOverride: SuggestionScope
            }
        }
    });
});
