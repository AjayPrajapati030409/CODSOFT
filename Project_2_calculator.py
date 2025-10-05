def add(a,b):
    return(a+b)

def div(a,b):
    return(a/b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def mod(a,b):
    return(a%b)

print("\n                             CALCULATOR                             \n")

print("Enter choice:\n","1: Addition\n","2: Division\n","3: Subtraction\n",
      "4: Multiplication\n","5: Modulus\n")
num=int(input())
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if num==1:
    print("Addition: ",add(a,b))
    

elif num==2:
    print("Division: ",div(a,b))
    

elif num==3:
    print("Subtraction: ",sub(a,b))
    

elif num==4:
    print("Multiplication: ",mul(a,b))
    

elif num==5:
    print("Modulus: ",mod(a,b))
    
else:
    print("Invalid")
