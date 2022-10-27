#The isinstance() function returns True if the specified object is of the specified type, otherwise False
    #Check if the number 5 is an integer:
x = isinstance(5, int)

    #Check if "Hello" is one of the types described in the type parameter:
x = isinstance("Hello", (float, int, str, list, dict, tuple))

#Parameter Values
    #Parameter	Description
    #object	Required. An object.
    #type	A type or a class, or a tuple of types and/or classes
    
    #Check if y is an instance of myObj:
class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj)
