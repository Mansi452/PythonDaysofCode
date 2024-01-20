#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_Upper_Lower(string):
    upperCount, lowerCount = 0, 0
    for char in string:
        if char.isalpha():
            if char.isupper():
                upperCount+=1
            elif char.islower():
                lowerCount+=1
    
    return (upperCount,lowerCount)



if __name__ == "__main__":
    string = input("Please enter the striing: ")
    upCount, lowCount = count_Upper_Lower(string)

    if upCount == lowCount == 0:
        print("There are no Upper and Lower case characters in the string.")
    elif upCount == 0 and lowCount != 0:
        print("There are no Upper case characters in the string. \n Number of lower case character in string is: {}.".format(lowCount))
    elif lowCount == 0 and upCount!=0:
        print("There are no Lower case characters in the string. \n Number of upper case character in string is: {}.".format(upCount))
    else:
        print("Number of Upper case character is string is : {}. \n Number of Lower case character is string is : {}.".format(upCount,lowCount))