def check_value(num):
        if num > 0:
            print("Number is Positive.")
        elif num < 0:
            print("Number is Negative")
        elif num == 0:
            print("Number is zero")
    
if __name__ == "__main__":
    try:
        num = int(input("Please enter the value to be added to the list: "))
        check_value(num)
    except ValueError:
        print("Please enter a valid number the next time")