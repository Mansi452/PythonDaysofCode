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
    n = int(input("Enter the number of elements in the list: "))
    if n == 0:
        print("Sum of elements is : 0.")
    else:
        lstValues = get_values(n)
        minVal, maxVal = min_max_values(lstValues)

        print("Minimum Value in the list is: ",minVal)
        print("Maximum Value in the list is: ",maxVal)