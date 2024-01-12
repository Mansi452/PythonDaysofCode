from math import pi,pow

def areaOfCircle(rad):
    try:
        rad = int(rad)
        return (pi * pow(rad,2))
    except ValueError:
        print("Please input only numerical values. Please try again!")
        


if __name__ == "__main__":
    rad = input("Please enter the radius of circle: ")
    area = areaOfCircle(rad)
    print("Area of the Circle with the radius ", rad, " unit is: ", area, " square unit.")
    
    