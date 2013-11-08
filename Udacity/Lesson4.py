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
        

#------NETWORKS

whatIsANetwork = """A newtwork is a group of entities that can communicate,
                    even though they are not all directly connected """
        
    
latency = "time it takes message to get from source to destination, measured in milliseconds"

bandwith = "amount of information that can be transmitted per unit time, measured in bits per second"