$(window).ready(function() {
    // Highlight current site and section in site header
    var baseFolder = window.document.location.pathname.split('/')[1];
    $('#jsDevDocs').addClass('currentSite');
    // console.log('The baseFolder is: ' + baseFolder);
    switch(baseFolder) {
        case 'api-explorer':
            $('#apiExplorerMenu > a').addClass('currentSection');
            break;
        case 'glossary':
            console.log('Got the glossary');
            $('header .middleHeader nav ul.menu li#glossaryMenu a').addClass('currentSection');
            break;
        case 'pages':
            $('#pagesMenu > a').addClass('currentSection');
            break;
        default:
            $('#pagesMenu > a').addClass('currentSection');
    }

    // Dynamically completing the ID based URL with the page path and title
    var location = window.document.location;
    var host = location.host;
    var originalSearch = location.search;
    var isExtUrl = originalSearch.includes("extUrl=1");
    // Complete URL only when on staging or with the ?extUrl=1 query parameter
    if (host == "d3in5cp0cx0iu6.cloudfront.net" || isExtUrl ) {
        var originalPath = location.pathname;
        // Remove any extended URI from originalPath
        var nativePath = originalPath.replace(/^(\/[0-9]*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$/,"$1$3");
        var originalHash = location.hash;

        var title = $('head > title').text();
        var codedTitle = title.replace(/([~!@#$%^&*()_+=`{}\[\]\|\\:;'<>,.\/? ])+/g, '-').replace(/^(-)+|(-)+$/g,'');
        var sourcePath = $('meta[name=sourcePath]').attr("content");
        var collectionLabel = sourcePath.substr(0, sourcePath.indexOf('/')).replace(/^_/, '');
        window.history.pushState("", "", nativePath + collectionLabel + '/' + codedTitle + originalHash + originalSearch);
    }

});