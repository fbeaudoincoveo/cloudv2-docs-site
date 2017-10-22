# Custom Liquid tag plugin to return an array containing the page TOC level indices needed to build the TOC and the breadcrumb
# 
# Usage: {% PageTocIndices %}
# Returns:  [i0,...,in]
# To be used ex.: pageInToc = toc["entries"][i0]["subentries"][i1]["subentries"][i2]["title"]
# 
# Created 2017-10-20 
# By FDallaire
# Inspired by: 
# - http://www.createdbypete.com/articles/create-a-custom-liquid-tag-as-a-jekyll-plugin/
# - https://blog.sverrirs.com/2016/04/custom-jekyll-tags.html

# Inherit from Liquid::Tag
module Jekyll
  class PageTocIndices < Liquid::Tag
    # Tag initializing
    def initialize(tag_name, input, tokens)
      super
      @indices = $tocIndices
    end
    
    # Lookup allows access to the page/post variables through the tag context
    def lookup(context, name)
      lookup = context
      name.split(".").each { |value| lookup = lookup[value] }
      lookup
    end
  
    # Global variable initializing 
    $tocLevel = 0                 # Indice of current TOC hierarchy level
    $iterations = 0               # Indice of TOC item in a TOC level
    $tocIndices = []              # Indices of the page for each TOC level
    $found = false                # Flag to break out of recursive loops
    $tocFolder = "_data/tocs/"    # Folder hosting the YAML TOC files
  
    # Recursively building the page position in TOC in the $tocIndices array
    def getIndices(entry)
      # Return if page already found
      if $found
        return
      end
      # Setting the TOC level
      l = $tocLevel
      
      # Recording the current item in the current TOC level
      $tocIndices[l] = $iterations
      
      puts "entry: " + entry["path"] + " \tl = " + l.to_s + " \ti = " + $iterations.to_s + "\t" + $tocIndices.to_s
      
      if ($pageUrl == entry["path"])
        # This is the page => break out
        puts "Indices when found: " + $tocIndices.to_s
        $found = true
        return
      elsif entry["subentries"]
        # Entering another TOC level
        $tocLevel += 1      # Increase TOC level
        $iterations = 0     # Reset item indice
        # Recursively call the method for each subentry
        entry["subentries"].each do |subentry|
          # Break if page already found
          if $found
            break
          end
          getIndices(subentry)
        end
        # Exiting a TOC level 
        $tocLevel -= 1                                # Decrease TOC level
        $iterations = $tocIndices[$tocLevel] + 1      # Increase item indice restored from previous TOC level
        if !$found
          $tocIndices = $tocIndices.first($tocLevel)  # Reduce the $tocInces array length
        end
        
      else
        # Go to next item in TOC level 
        $iterations += 1
      end
      puts "Indices at if end: " + $tocIndices.to_s
    end
  
    def render(context)
      # Accessing the page/site variable for the base url
      $pageUrl = "#{lookup(context, 'page.url')}"
      pagePath = "#{lookup(context, 'page.path')}"
      tocName = pagePath.split(/\//).first.sub!("_", "")
      tocFile = $tocFolder + tocName + ".yml"
  
      require 'yaml'
      # Load the YAML toc and its entries
      toc = YAML.load_file(tocFile)
      entries = toc["entries"]
      
      # tocLevelIndex(entries)
      entries.each do |entry|
        # Break if page already found
        if $found
          break
        end
        getIndices(entry)
      end
  
      # Build the output
      output = $tocIndices.to_s
      # Render it on the page by returning it
      #$tocIndices
      return output
    end
  end  
end

# Register the new custom Liquid tag
Liquid::Template.register_tag('PageTocIndices', Jekyll::PageTocIndices)