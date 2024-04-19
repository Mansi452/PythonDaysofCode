#Write a program that capitalizes the first letter of each word in a sentence.

def capitalize_word(lstString):
    temp = []

    for word in lstString:
        temp.append(word.capitalize())
    
    sentence = " ".join(temp)
    print(sentence)

if __name__ == "__main__":
    x = input("Please enter the string separated by spaces: ")
    lstString = x.split(' ')
    capitalize_word(lstString)