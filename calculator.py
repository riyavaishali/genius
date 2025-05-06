def add(a,b):
    sum=a+b
    return sum
def  subtract(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c

l=["Addition","Subtraction","Multiplication","Division"]
for i in range(len(l)):
    print(l[i])

print(" ")

while True:
    opt=input("enter option  ")
    a=int(input("enter first number  "))
    b=int(input("enter second number  "))
    if opt in l:
       if opt==l[0]:
           print("Addition= ",add(a,b))
           print(" ")
       elif opt==l[1]:
           print("Subtraction= ",subtract(a,b))
           print(" ")
       elif opt==l[2]:
           print("Multiplication= ",multiply(a,b))
           print(" ")
       else :
           print("Division= ",division(a,b))
           print(" ")
       next_opt=input("Do you want to select another option ? ")
       print(" ")
       if next_opt=='no':
           print("Thank you")
           break
    else:
        print("Invalid input")
    