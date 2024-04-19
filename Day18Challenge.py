#Write a program to find the largest among three numbers.

def max_of_three(lstNum):
    maxValue = float('-inf')

    for num in lstNum:
        if num > maxValue:
            maxValue = num
    print("Max of the three is: ", maxValue)
    

if __name__ == "__main__":
    i = 0
    lstNum = []
    while i < 3:
        try:
            n = int(input("Enter the number to be compared: "))
            lstNum.append(n)
            i+=1
        except ValueError:
            print("Please eneter valid value. ")
    
    max_of_three(lstNum)
    
