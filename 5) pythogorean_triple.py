print("enter the number in increasing order")
a=eval(input("enter the first number\n"))
b=eval(input("enter the second number\n"))
c=eval(input("enter the third number\n"))
d=a^2+b^2
e=c^2
if d==e:
    print(f"the entered numbers {a},{b},{c} are the pythogoren triple")
else:
    print(f"the entered number {a},{b},{c} are not the pythogoren triple")    
