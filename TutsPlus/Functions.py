#!/user/bin/env python

def madlib(adjective, name='dillon'):
    print "the %s %s ate all the pizza" % (adjective, name)
    
#madlib('hungry','brad')
#madlib(adjective='fat',name='blaine')
'''
def shoppingCart(itemName, **avgPrices):
    for store in avgPrices:
        print store, 'price: ',avgPrices[store]
'''
    
def shoppingCart(itemName, avgPrices):
    print 'item: ', itemName
    for store in avgPrices:
        print store, 'price: ',avgPrices[store]   
#shoppingCart('computer',amazon=100,ebay=120,bestBuy=34)

def dbLookup():
    dict = {}
    dict['amazon']=100
    dict['ebay']=120
    dict['bestbuy']=34
    return dict

#print dbLookup()
shoppingCart('computer', dbLookup())