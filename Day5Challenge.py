#Write a program to find the maximum and minimum values in a list.

def get_values(n):
    lstValues = []
    i = 0
    while i < n:
        try:
            lstValues.append(int(input("Please enter the value to be added to the list: ")))
            i+=1
        except ValueError:
            print("Please eneter valid value. ")

    return lstValues


def min_max_values(lstValues):
    minVal = float('inf')
    maxVal = float('-inf')

    for num in lstValues:
        minVal = min(num,minVal)
        maxVal = max(num,maxVal)
    
    return (minVal,maxVal)  

if __name__ == "__main__":
    x = input("Enter the number of elements in the list: ")
    try:
        n = int(x)
        if n == 0:
            print("No elements in the list to find the minimum and maximum elements.")
        else:
            lstValues = get_values(n)
            minVal, maxVal = min_max_values(lstValues)

            print("Minimum Value in the list is: ",minVal)
            print("Maximum Value in the list is: ",maxVal)
    except ValueError:
        print("Please enter valid number!")