#!/usr/bin/ruby
# Adds or resets the id (slug: "n") to the front matter of each Markdown file of a folder and to the specified idFile.
# The YAML idFile must exist and contain at least the following:
#
# items:
#
# usage:    AddIdToAllMarkdownFilesInAFolder.rb sourceFolder ifFile userName
# ex:       scripts/AddIdToAllMarkdownFilesInAFolder.rb "_ccv2-dev" "_data/ids_test.yml" "fdallaire"

sourceFolder = ARGV[0]
idFile = ARGV[1]
userName = ARGV[2]

require 'yaml'

# Load the YAML ifFile and its items
ids = YAML.load_file(idFile)
items = ids['items']

# Find the highest used id value
highestId = 0 
items.each do |n|
    itemId = n['id'].to_i
    if itemId > highestId
        highestId = itemId
    end
end
newId = highestId + 1
puts 'Original new ID: ' + newId.to_s

# Open the idFile in append mode
File.open(idFile,'a') do |h| 

    # Iterate through a folder to set the ID in Markdown front matter slug parameter
    Dir.foreach(sourceFolder) do |file|
        # Ignore current and parent folders
        next if file == '.' or file == '..' or !file.include? ".md"
        
        filePath = sourceFolder + '/' + file
        # Remove leading '../' occurrences from file path
        rootFilePath = filePath.gsub(/^(\.\.\/)+/,'/')
                
        # Check if file already has an id
        hasId = false
        items.each do |n|
            itemPath = n['path']
            # puts "itemPath = " + itemPath + "| rootFilePath = " + rootFilePath
            if itemPath == rootFilePath
                hasId = true
            end
        end
        
        # When the file does not yet have an ID
        if !hasId
            # Read the file text content
            text0 = File.read(filePath)
            # Remove existing 'slug' front matter entries
            text1 = text0.gsub(/^slug:\s*["']([0-9]*)["'](.*)\n/,"")  
            # Add 'slug' value as first front matter entry
            slugId = 'slug: "' + newId.to_s + '"'
            text2 = text1.gsub(/\A(---)\s*/, "---" + "\n" + slugId + "\n")

            # Write the modified text to the file
            puts "Writing to " + filePath
            File.open(filePath, "w") {|f| f.puts text2 }

            # Write file information in idFile
            h.puts ''
            h.puts '- id: ' + newId.to_s
            h.puts '  path: ' + rootFilePath
            h.puts '  createddate: ' + Time.now.getutc.localtime.strftime('%Y-%m-%dT%H:%M:%S%z')
            h.puts '  createdby: ' + userName
            h.puts '  lastmodifieddate: '
            h.puts '  lastmodifiedby: '
            newId = newId + 1
        else 
            puts 'File (' + rootFilePath + ') already has an ID'
        end

        puts 'New ID: ' + newId.to_s
    end
end
