#Write a program to check if a number is even or odd.

def check_odd_even(num):
        if num %2== 0:
            print("Number is Even.")
        else:
            print("Number is Odd.")
    
if __name__ == "__main__":
    try:
        num = int(input("Please enter the number to be checked: "))
        check_odd_even(num)
    except ValueError:
        print("Please enter a valid number the next time")