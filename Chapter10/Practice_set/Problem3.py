'''
Create a class with a class attribute a; create an object from it and set 'a'
direclty using object. a = 0. Does this change the class attribute.
'''

class Demo:
    a = 4

o = Demo()
print(o.a) # Print the class attribute because instance attribute is not present 
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute beacause instance attribute is present 
print(Demo.a) # prints the class attribute
# Class attribute has not change but set a instance
