from math import pi,pow

def area_of_circle(rad):
    try:
        rad = int(rad)
        return (pi * pow(rad,2))
    except ValueError:
        print("Please input only numerical values. Please try again!")
        return



if __name__ == "__main__":
    rad = input("Please enter the radius of circle: ")
    area = area_of_circle(rad)
    if area != None:
        print("Area of the Circle with the radius ", rad, " unit is: ", area, " square unit.")
    
    