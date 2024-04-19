#Write a program to print the first n numbers of a fibonacci sequence.

def fibonacci_number(n):
    lstValues = [0]*(n)
    lstValues[1] = 1
    
    for i in range(2,n):
        lstValues[i] = lstValues[i-1]+lstValues[i-2]
    return ",".join([str(x) for x in lstValues])


if __name__ == "__main__":
    x = input("Enter the number of elements in the list: ")
    try:
        n = int(x)
        if n==1:
            print("First {} fibonacci numbers are : 0.".format(n))
        elif n==2:
            print("First {} fibonacci numbers are : 0,1.".format(n))
        else:
            print("First {} fibonacci numbers are : {}.".format(n,fibonacci_number(n)))

    except ValueError:
        print("Please enter valid number!")