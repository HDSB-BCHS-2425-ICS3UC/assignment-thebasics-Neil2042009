import math
def cube1():
    length = float (input("Enter the length of your cube: "))
    return length **3
#This is to let user enter the value of the length of their cube
def sphere1():
    sphere = float (input("Enter the radius of your sphere: "))
    return (3/4)*math.pi*sphere**3
#This is to let user enter the value of the radius of their sphere
def cone1():
    cone = float (input("Enter the radius of your cone: "))
    h = float (input("Enter the height of your cone: "))
    return (3/4)*math.pi*cone**2*h
#This is to let user enter the value of the radius and height of their cone
def cylinder1():
    cylinder = float (input("Enter the radius of your cylinder: "))
    h = float (input("Enter the height of your cylinder: "))
    return math.pi*cylinder**2*h
#This is to let user enter the value of the radius and height of their cylinder


def main():
    print("Hello, dear user, welcome to the volume of the three-dimensional shapes calculator.")
    print("Selcet the 3D sahpe you want to calculate the volume.")
    choice=input("If you want to choose Cube press 0, Sphere press 1, Cone press 2, Cylinder press 3:")
   #These are choices and if user enter these numbers it will bring them to calculate.
    if choice =='0':
        volume = cube1()
        print (f"The volume of the cube is: {volume}")

    elif choice =='1':
        volume1 = sphere1()
        print (f"The volume of the sphere is: {volume1}")

    elif choice =='2':
        volume2 = cone1()
        print (f"The volume of the cone is: {volume2}")

    elif choice =='3':
        volume3 = cylinder1()
        print (f"The volume of the cylinder is: {volume3}")
    
    else:
        print("Invalid input! Try again.")
#If user entered something else it's going to show let thise string.
if __name__=="__main__":
    main()
#Author: Neil
#Date Modified: February 28, 2025
#Description: Calculate the volume of 3Ds
