##
# Monkey patch Jekyll's Page and Post classes (from https://biosphere.cc/software-engineering/jekyll-breadcrumbs-navigation-plugin/)
#
module Jekyll
    
        class Page
            def ancestors
                get_pages(self.path)
            end
            
            ##
            # Make ancestors available.
            def to_liquid(attrs = ATTRIBUTES_FOR_LIQUID)
                super(attrs + %w[
                    ancestors
                ])
            end
        end
    
        class Post
            def ancestors
                get_pages(self.path)
            end
    
            ##
            # Make ancestors available.
            def to_liquid(attrs = ATTRIBUTES_FOR_LIQUID)
                super(attrs + %w[
                    ancestors
                ])
            end
        end
    end
    
    ##
    # Returns ordered list 
    def get_pages(path)
        a = []
        while path != "index.md"
            pt = path.split("/")
            # puts 'pt array: ' + pt.to_s
            if pt[-1] != "index.md"
                # to to directory index
                pt[-1] = "index.md"
                path = pt.join("/")
            else
                # one level up
                path = pt[0..-3].join("/") + "/index.md"
            end
            a << get_page_from_path(path)
        end
        a.reverse
    end
    
    ##
    # Gets Page object that has given path. Very inefficient O(n) solution.
    def get_page_from_path(path)
        (site.pages).each do |page|
            return page if page.path == path
        end
    end