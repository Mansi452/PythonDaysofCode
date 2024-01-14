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
    
def sum_list(lstValues):
    summ = 0
    for val in lstValues:
        summ += val
    
    return summ

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    if n == 0:
        print("Sum of elements is : 0.")
    else:
        lstValues = get_values(n)
        sumValues = sum_list(lstValues)

        print("Sum of the list of integers: ", sumValues)
