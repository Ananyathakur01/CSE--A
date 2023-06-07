a=eval(input("enter the first side of the triangle\n"))
b=eval(input("enter the second side of the triangle\n"))
c=eval(input("enter the third side of the triangle\n"))
d=a+b+c
if d==180:
    print(f"the given sides {a},{b},{c} can form a triangle")
else:
    print(f"the given sides {a},{b},{c} cannot form a triangle")
        