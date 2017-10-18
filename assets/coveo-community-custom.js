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

    // Dynamically completing the ID based URL with the page path and title if extUrl=1
    var originalPath = window.document.location.pathname;
    var originalHash = window.document.location.hash;
    var originalSearch = window.document.location.search;
    var isExtUrl = originalSearch.includes("extUrl=1");
    var title = $('head > title').text();
    var codedTitle = title.replace(/([~!@#$%^&*()_+=`{}\[\]\|\\:;'<>,.\/? ])+/g, '-').replace(/^(-)+|(-)+$/g,'');
    var sourcePath = $('meta[name=sourcePath]').attr("content");
    var collectionLabel = sourcePath.substr(0, sourcePath.indexOf('/')).replace(/^_/, '');
    if (isExtUrl) {
        window.history.pushState("", "", originalPath + collectionLabel + '/' + codedTitle + originalHash + originalSearch);
    }
});