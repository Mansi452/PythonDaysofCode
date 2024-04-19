# Write a program that checks if a year is a leap year.
def check_leap_year(n):
    if (n % 400 == 0) or (n%100 != 0 and n%4 == 0):
        print("The given year is a leap year.")
    else:
        print("The given year is not a leap year.")


if __name__ == "__main__":
    x = input("Enter the year to be checked: ")
    try:
        check_leap_year(int(x))

    except ValueError:
        print("Please enter valid number!")