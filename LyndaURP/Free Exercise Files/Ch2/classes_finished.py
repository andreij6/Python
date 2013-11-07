#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

class myClass():
  def method1(self):
    print "myClass method1"
    
  def method2(self, someString):
    print "myClass method2: " + someString
    
class anotherClass(myClass):                    #inherits form myClass
  def method2(self):                            #Overrides method2 from Class1
    print "anotherClass method2"
    
  def method1(self):                            #Overrides method1 from Class1
    myClass.method1(self);
    print "anotherClass method1"
      
def main():
  c = myClass()
  c.method1()                           #myClass method1
  c.method2("This is a string")         #myClass method2: This is a string
  c2 = anotherClass()
  
  c2.method1()                          #myClass method1
                                        #anotherClass method1
  
  c2.method2()                    #anotherClass method2
  
if __name__ == "__main__":
  main()
