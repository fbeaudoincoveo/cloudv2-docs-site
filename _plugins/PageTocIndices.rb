# Custom Liquid tag plugin to return an array containing the page TOC level indexes
# 
# Usage: {% PageTocIndices %}
# 
# Assumes the toc file is under _data/tocs
#
# Created 2017-10-20 
# By FDallaire
# Inspired by: 
# - http://www.createdbypete.com/articles/create-a-custom-liquid-tag-as-a-jekyll-plugin/
# - https://blog.sverrirs.com/2016/04/custom-jekyll-tags.html

# Inherit from Liquid::Tag
class PageTocIndices < Liquid::Tag
    def initialize(tag_name, input, tokens)
      super
    end
   
    $tocLevel = 0
    $iterations = 0
    $tocIndices = []
    $found = false
    
    # Lookup allows access to the page/post variables through the tag context
    def lookup(context, name)
      lookup = context
      name.split(".").each { |value| lookup = lookup[value] }
      lookup
    end

    # Function to build the page toc indices
    # def tocLevelIndex(toc)
    #   i = 0
    #   l = $tocLevel
    #   puts "l= " + l.to_s
    #   $tocIndices = $tocIndices.first(l)
    #   toc.each do |entry|
    #     $tocIndices[l] = i
    #     # t = t + "entry: " + entry["path"] + " | pageUrl: " + $pageUrl + "\n"  
    #     # puts entry.to_s
    #     puts "entry: " + entry["path"] + " | pageUrl: " + $pageUrl + "\n"
    #     puts $tocIndices.to_s 
    #     if ($pageUrl == entry["path"])
    #       $found = true
    #       return
    #     elsif entry["subentries"]
    #       # puts 'subentries for ' + i.to_s + " tocLevel: " + $tocLevel.to_s + entry.to_s + 
    #       $tocLevel += 1
    #       tocLevelIndex(entry["subentries"])
    #       $tocLevel -= 1
    #     end
    #     i += 1
    #   end
    # end
  
    def tocLevelIndex2(entry)
      l = $tocLevel
      $tocIndices[l] = $iterations
      puts "entry: " + entry["path"] + " \tl = " + l.to_s + " \ti = " + $iterations.to_s + "\t" + $tocIndices.to_s
      # puts "entry: " + entry["path"] + " | pageUrl: " + $pageUrl + "\n"
      if ($pageUrl == entry["path"])
        $found = true
        puts "THIS IS THE TOPIC!" + " | found = " + $found.to_s
        return
      elsif entry["subentries"]
        $tocLevel += 1
        $iterations = 0
        entry["subentries"].each do |subentry|
          if $found
            break
          end
          tocLevelIndex2(subentry)
        end
        $tocLevel -= 1
        $iterations = $tocIndices[$tocLevel] + 1
        $tocIndices = $tocIndices.first($tocLevel)
      else
        $iterations += 1
      end
    end

    def render(context)
      # Accessing the page/site variable for the base url
      $pageUrl = "#{lookup(context, 'page.url')}"
      pagePath = "#{lookup(context, 'page.path')}"
      tocName = pagePath.split(/\//).first.sub!("_", "")
      tocFile = "_data/tocs/" + tocName + ".yml"

      require 'yaml'
      # Load the YAML toc and its entries
      toc = YAML.load_file(tocFile)
      entries = toc["entries"]
      
      # tocLevelIndex(entries)
      entries.each do |entry|
        if $found
          break
        end
        tocLevelIndex2(entry)
      end

      # Build the output
      tocEntryEx1 = toc["entries"][3]["subentries"][3]["subentries"][0]["title"]
      output = $tocIndices.to_s
      # output = "i = " + tocLevelIndex.to_s + " | tocIndices = " + $tocIndices.to_s
      # output =  "Title of first TOC entry: " + tocEntryEx1
      # output = "tocFile: " + tocFile + " | pageUrl: " + pageUrl + " | pagePath: " + pagePath + + " | tocName: " + tocName
      # Render it on the page by returning it
      return output;
    end

end

# Register the new custom Liquid tag
Liquid::Template.register_tag('PageTocIndices', PageTocIndices)