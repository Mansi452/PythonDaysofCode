#Write a program that swaps the values of two variables.

def swap_values(a,b):
    a, b = b, a
    return (a,b)


if __name__ == "__main__":
    a = input("Please input the first variable value: ")
    b = input("Please input the second variable value: ")

    c,d = swap_values(a,b)

    print("The old values of the variables are : ", a, " and ",b,".")
    print("The new values of the variables are : ", c, " and ",d,".")

