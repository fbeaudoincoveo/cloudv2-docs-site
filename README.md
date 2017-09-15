#READ ME

## Installation
1. Install Jekyll.
   
   The Coveo Docs Site is generated with Jekyll, so you must install Jekyll and its requirements such as Ruby. 
   Tom Johnson's installation procedure work: 
   - [Install Jekyll on Mac](http://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_mac.html)
   - [Install Jekyll on Windows](http://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_windows.html)


## Build and Test Site locally
Build the site locally to validate your changes: 
1. In the terminal, run ```bundle exec jekyll serve --baseurl ''```
1. Go to `http://localhost:4000/` to view the site. 
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

## Contribution Guidelines
Upcoming...
