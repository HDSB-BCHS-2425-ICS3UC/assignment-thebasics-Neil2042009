import math
Cube = 0
Sphere = 1
Cone = 2
Cylinder = 3
choice = float(input())

def cube1():
    length = float (input("Enter the length of your cube "))
    return length **3

def sphere1():
    sphere = float (input("Enter the radius of your sphere "))
    return (3/4)*math.pi*sphere**3

def cone1():
    cone = float (input("Enter the radius of your cone "))
    h = float (input("Enter the height of your cone "))
    return (3/4)*math.pi*cone**2*h

def cylinder1():
    cylinder = float (input("Enter the radius of your cylinder "))
    h = float (input("Enter the height of your cylinder "))
    return math.pi*cylinder**2*h



def main():
    print("Hello, dear user, welcome to the volume of the three-dimensional shapes calculator.")
    print("Selcet the 3D sahpe you want to calculate the volume.")
    print("If you want to choose Cube press 0, Sphere press 1, Cone press 2, Cylinder press 3.")
    
    if choice == "0":
        volume = cube1()
        lenght = float (input("Enter the length of your cube "))

    elif choice =='1':
        volume = sphere1()
        sphere = float (input("Enter the radius of your sphere "))

    elif choice =='2':
        volume = cone1()
        cone = float (input("Enter the radius of your cone "))
        h = float (input("Enter the height of your cone "))

    elif choice =='3':
        volume = cylinder1()
        cylinder = float (input("Enter the radius of your cylinder "))
        h = float (input("Enter the height of your cylinder "))