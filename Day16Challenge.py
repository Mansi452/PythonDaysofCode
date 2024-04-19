#Write a function that counts the frequency of each word in a sentence.

def count_frequency(lstString):
    dictFreq = {}

    for word in lstString:
        word = word.lower()
        dictFreq[word] = dictFreq.get(word,0)+1
    
    print(dictFreq)

if __name__ == "__main__":
    x = input("Please enter the string separated by spaces: ")
    lstString = x.split(' ')
    count_frequency(lstString)