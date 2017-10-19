# Custom Liquid tag plugin to return the page parent url from a TOC
# 
# Usage: {% PageTocParent %}
# 
# Assumes the toc file is under _data/tocs
#
# Created 2017-10-18 
# By FDallaire
# Inspired by: 
# - http://www.createdbypete.com/articles/create-a-custom-liquid-tag-as-a-jekyll-plugin/
# - https://blog.sverrirs.com/2016/04/custom-jekyll-tags.html

# Inherit from Liquid::Tag
class PageTocParent < Liquid::Tag
    def initialize(tag_name, input, tokens)
      super
    end
   
    # Lookup allows access to the page/post variables through the tag context
    def lookup(context, name)
      lookup = context
      name.split(".").each { |value| lookup = lookup[value] }
      lookup
    end
  
    def render(context)
      # Accessing the page/site variable for the base url
      pageUrl = "#{lookup(context, 'page.url')}"
      pagePath = "#{lookup(context, 'page.path')}"
      tocName = pagePath.split(/\//).first.sub!("_", "")
      tocFile = "_data/tocs/" + tocName + ".yml"

      require 'yaml'
      # Load the YAML toc and its entries
      ids = YAML.load_file(tocFile)
      entries = ids['entries']

      # Find the page parent URL (ex: /123/)
      parentUrl = "/0/" 
      entries.each do |e|
          itemId = e['id']
          if itemId > highestId
              highestId = itemId
          end
      end

      # Write the output
      output = "pageUrl: " + pageUrl + " | pagePath: " + pagePath + + " | tocName: " + tocName
      # Render it on the page by returning it
      return output;
    end

    def split_params(params)
      params.split("|")
    end
end


# Register the new custom Liquid tag
Liquid::Template.register_tag('PageTocParent', PageTocParent)