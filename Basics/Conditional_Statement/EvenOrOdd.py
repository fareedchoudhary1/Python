# find a number is even or odd without using modulas.

a = int(input("Enter number:"))
r = a-2*(a//2)
if(r == 0):
    print("Even")
else:
    print("Odd")