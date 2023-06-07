print("To calculate the surface volume of cylinder and area of cylinder enter its radius and height")
radius=eval(input("enter the radius\n"))
height=eval(input("enter the height\n"))
PI=3.14
volume=PI*radius*radius*height
SurfaceAreaOfCylinder=((2*radius)*height)+((PI*radius*2)*2)
print("Surface volume of cyliner is", volume," Area of cylinder is " , SurfaceAreaOfCylinder)