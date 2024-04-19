# Write a program to reverse a given string

def reverse_string(string):
    left, right = 0, len(string)-1

    while left < right:
        string[left],string[right] = string[right],string[left]
        left+=1
        right -=1
    
    return ''.join(string)

if __name__ == "__main__":
    string1 = input("Please enter the string: ")
    if len(string1) == 0:
        string2 = ""
        print("The input string is : {}. \n The reveresed string is : {}.".format(string1,string2))
    else:
        # print(list(string1))
        string2 = reverse_string(list(string1))
        print("The input string is : {}. \n The reveresed string is : {}.".format(string1,string2))