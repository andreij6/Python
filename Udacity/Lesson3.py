p = [0, 1, 2]
q = [2,4,5]

print 2 in p                        #true

print 3 not in p                    #true

    #Define find_element using index

def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1
    
print find_element([1,2,3],2)       #1

    #Define union procedure

def union(p,q):
    for item in q:
        if item not in p:
            p.append(item)
    print p
    
union(p,q)

#---POP---------------

#<list>.pop() -> element
 
p.pop()
p.append(3)
print p

#---- RECAP OF WEBCRAWLER CODE WE HAD AT THE end of unit 2

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote   = page.find('"', start_quote + 1)
    url         = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True: 
        url, endpos = get_next_target(page)
        if url:
            print url
            page    = page[endpos:]
        else: 
            break

#----------get_all_links
def get_all_links(page):
    links = []
    while True: 
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page    = page[endpos:]
        else: 
            break
    return links

#---------crawl_web

def get_page():
    return 0

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

