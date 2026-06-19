# Create a calculator using if-else statement

a = float(input("Enter first value:"))
b = float(input("Enter second value:"))
c = input("Enter operation(+,-,*,/,**):")
if(c=="+"):
    print("Result:",a+b)
elif(c=="-"):
    print("Result:",a-b)
elif(c=="*"):
    print("Result",a*b)
elif(c=="/"):
    print("Result",a/b)
elif(c=="**"):
    print("Result",a**b)
else:
    print("Invalid operation") 