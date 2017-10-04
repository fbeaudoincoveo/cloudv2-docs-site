$(window).ready(function() {
    // Highlight current site and section in site header
    var baseFolder = window.document.location.pathname.split('/')[1];
    $('#jsDevDocs').addClass('currentSite');
    console.log('The baseFolder is: ' + baseFolder);
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

    // Injecting the page title in the glossary ID based URL
    var title = $('head > title').text();
    var codedTitle = title.replace(/([~!@#$%^&*()_+=`{}\[\]\|\\:;'<>,.\/? ])+/g, '-').replace(/^(-)+|(-)+$/g,'');
    var originalPath = window.document.location.pathname;
    var originalHash = window.document.location.hash;
    if (originalPath.includes('/glossary/') ) {
        window.history.pushState("", "", originalPath + codedTitle + originalHash);
    }
});