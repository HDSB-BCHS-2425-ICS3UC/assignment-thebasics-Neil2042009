
import math 
print("Hello, dear user, welcome to the volume of the three-dimensional shapes calculator.")
print("Due to limited technology, our calculations will be performed in the order: Cube, Sphere, Cone and Cylinder")
print("If it is not the 3D object you need to calculate, please enter any number, click Enter, and repeat this step until you see the object you need to calculate.")

length = float (input("Cube: Enter the length of your cube: "))
#This is to let user enter the length of their cube.
result_cube = length **3
print (f"The volume of the cube is: {result_cube}")
#

sphere = float (input("Sphere: Enter the radius of your sphere: "))
#This is to let user enter the value of the radius of their sphere
result_sphere= (3/4)*math.pi*sphere**3
print (f"The volume of the sphere is: {result_sphere}")
#

cone = float (input("Cone: Enter the radius of your cone: "))
h = float (input("Enter the height of your cone: "))
#This is to let user enter the value of the radius and height of their cone    
result_cone = (3/4)*math.pi*cone**2*h
print (f"The volume of the cone is: {result_cone}")
#

cylinder = float (input("Cylinder: Enter the radius of your cylinder: "))
h = float (input("Enter the height of your cylinder: "))
#This is to let user enter the value of the radius and height of their cylinder
result_cylinder=math.pi*cylinder**2*h
print (f"The volume of the cylinder is: {result_cylinder}")

#Author: Neil
#Date Modified: February 28, 2025
#Description: Calculate the volume of 3Ds