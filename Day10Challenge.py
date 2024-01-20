#Write a program to remove duplicates from a list.

def get_values(n):
    lstValues = []
    for _ in range(n):
        lstValues.append((input("Please enter the value to be added to the list: ")))
    return lstValues

def remove_duplicates(lstValues):
    uniqueValue = set()
    i = 0
    while i < len(lstValues):
        num = lstValues[i]
        if num not in uniqueValue:
            uniqueValue.add(num)
            i+=1
        else:
            lstValues.pop(i)

    return lstValues
    
    
if __name__ == "__main__":
    x = input("Enter the number of elements in the list: ")
    try:
        n = int(x)
        lstValues = get_values(n)
        updatedList = remove_duplicates(lstValues)

        print("Updated list after removing the duplicates: ",updatedList)
    except ValueError:
        print("Please enter valid number!")
    