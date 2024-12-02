import sys

# check python version
print(sys.version)
# print("hello word")
# end termial when done

"""
 ifelse
if 1 > 5:
    print("1 was 5")
if 5 > 1: 
    print("5>1")    
"""

#  create variable values 
#  x = 3 
#  y = 3
#  x1 = str(3)
#  y2 = int(3)

print(type(3)) #get data type of variable 


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # ===  print(x + y + z)

x = "1"
#create example function
def myFunction():
    x = "my function"
    print(x, 1)

# print     
myFunction()
print(x)   
# create global variable

myGlobalVariable = "awesome"

def  myGlobalFunction():
    
    global myGlobalVariable #  cannot set value

    myGlobalVariable ="test"
    print(myGlobalVariable)
myGlobalFunction()
print(myGlobalVariable)
 
a = 3
# print("heelo {a}" )

txt = f"The price is {a:.2f} dollars"

print(txt)

exit()