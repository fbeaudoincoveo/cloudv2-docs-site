// Highlight current site and section in site header

var baseFolder = window.document.location.pathname.split('/')[1];
$(window).ready(function() {
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
});

