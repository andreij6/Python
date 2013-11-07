#Data Structures

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

#--------third video

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])



def lookup(index,keyword):
    for item in index:
        if item[0] == keyword:
            return item[1]
    return []
    
def add_page_to_index(index, url, content):
    keys = content.split()
    for keyword in keys:
        add_to_index(index, keyword, url)
        
    
    