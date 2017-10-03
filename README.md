#READ ME

## Installation
1. Fork the repository locally. 
1. Install Jekyll.
   
   The Coveo Docs Site is generated with Jekyll, so you must install Jekyll and its requirements such as Ruby. 
   Tom Johnson's installation procedure work: 
   - [Install Jekyll on Mac](http://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_mac.html)
   - [Install Jekyll on Windows](http://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_windows.html)
1. Intall [html-proofer](https://github.com/gjtorikian/html-proofer) to allow testing external links in the content: 

   `gem install html-proofer`
   
1. Install [s3_website](https://github.com/laurilehmijoki/s3_website) to be able to push to AWS S3:
   
   `gem install s3_website`

## Build and Test Site locally

Build the site locally to validate your changes:
1. In the terminal: 
   1. Go to the repository root folder. 
   1. Run ```bundle exec jekyll serve --incremental```
   
      > Alternately:
      > - If you want sitemap.xml links to contain the production hostname (not localhost:4000), run:
      >
      >  ```JEKYLL_ENV=production bundle exec jekyll serve --incremental```
      >  
      >  The default value is `JEKYLL_ENV=development` (see [Specifying a Jekyll environment at build timePermalink](https://jekyllrb.com/docs/configuration/#specifying-a-jekyll-environment-at-build-time)). 
      >  
      > - If `baseurl` was not empty in `_config.yml` and you want to the local site to start from the root, run: 
      > 
      >  ```bundle exec jekyll serve --baseurl '' --incremental```
         
1. In a browser, go to `http://localhost:4000/` to view the site. 
1. Make your changes to the site. 
1. Validate your changes in the local site.
1. In the terminal, run the [HTML-Proofer](https://github.com/gjtorikian/html-proofer#whats-tested) to validate links, images, scripts and more are working .

   ```htmlproofer --assume-extension  --allow-hash-href --alt-ignore --check-external-hash ./_site```
   
   > Options:
   > - `--assume-extension` adds `.html` extensions to extensionless paths
   > - `--allow-hash-href` ignores the `<a href="#" ..>`occurrences
   > - `--alt-ignore` safely ignore image missing `alt` attributes
   > - `--check-external-hash` check bookmarks in  external links (can slow down the check)
1. In the terminal, run the [s3_website](https://github.com/laurilehmijoki/s3_website) command to push changes to the S3 `coveo-products-docs` bucket:
   `s3_website push`
1. Make a pull request to propose your changes. 

## Contribution Guidelines

See [CONTRIBUTING-CONTENT.md](CONTRIBUTING-CONTENT.md)

