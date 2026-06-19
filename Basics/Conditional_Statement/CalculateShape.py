# calculate:
# parameter of circle, 
# parameter of rectangle, 
# area of circle, 
# volume of cone,
# volume of vuboid


find= input("Calculate the:")
if(find == "parameter of circle"):
    r = float(input("Enter the radius:"))
    parameter = 2*3.14*r
    print(parameter)
elif(find == "parameter of rectangle"):
    l = float(input("Enter the length:"))
    w = float(input("Enter the width:"))
    p = 2*(l+w)
    print(p)
elif(find == "area of circle"):
    r = float(input("Enter the radius:"))
    area = 3.14*r*r
    print(area)
elif(find == "volume of cone"):
    r = float(input("Enter the radius:"))
    h = float(input("Enter the height:"))
    volume = 3.14*r*r*(h/3)
    print(volume)
elif(find == "volume of cuboid"):
    l = float(input("Enter the length:"))
    w = float(input("Enter the width:"))
    h = float(input("Enter the height:"))
    v = l*w*h
    print(v)
else:
    print("invalid input")