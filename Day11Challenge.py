#Write a program to print the multiplication table of a given number.

def print_table(num):
    print("Below is the multiplication for {}: ".format(num))
    for mul in range(1,11):
        print("{} * {} = {}".format(num,mul,num*mul))    

if __name__ == "__main__":
    try:
        num = int(input("Please enter the number to get the multiplication table: "))
        print_table(num)
    except ValueError:
        print("Please enter a valid number the next time")