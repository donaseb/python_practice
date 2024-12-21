import sys
import os
def addition(num1,num2):
    s=num1+num2
    return s
def sub(num1,num2):
    d=num1-num2
    return d
num1=int(sys.argv[1])
operation=sys.argv[2]
num2=int(sys.argv[3])
if operation =="add":
    output=addition(num1,num2)
    print(output) 
else:
    output=sub(num1,num2)
    print(output)
print(os.getenv("password"))
