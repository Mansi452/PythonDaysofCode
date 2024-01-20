#Write a function to count the number of vowels in a given string.

def count_vowels(string):
    counter = len([char for char in string if char in 'aeiouAEIOU'])

    return counter

if __name__ == "__main__":
    a = input("Enter the string to get the count of vowels: ")

    print("The number of vowels in the string gievn is: ", count_vowels(a))
    
    