languages = ['python','java','C++','PHP']

for language in languages:
    print language, "rocks!!"
    
contacts = {"language":"English", "location":"denver","favorite site":"espn.com"}

for key in contacts:
    print 'His', key, "is", contacts[key]
    
print range(10)

for inte in range(10):
    print "int = ", inte

count = 0 
while count < 10:
    print count, "is less than 10"
    count += 1
    
for i in range(10):
    print "i = ", i
    if i == 5:
        break
    
print "done looping"

for i in range(2):
    print "this is before continue"
    continue
    print "this is after the continue statement"
    
for i in range(2):
    pass
