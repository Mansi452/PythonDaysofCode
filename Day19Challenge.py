#Write a function to calculate the factorial of a number.

def cal_factorial(num):
        if num %2== 0:
            print("Number is Even.")
        else:
            print("Number is Odd.")
    
if __name__ == "__main__":
    try:
        num = int(input("Please enter the number to be checked: "))
        if num == 0 or num == 1:
             print("")
        cal_factorial(num)
    except ValueError:
        print("Please enter a valid number the next time")