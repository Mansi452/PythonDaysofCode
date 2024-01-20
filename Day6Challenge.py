def count_occurrence(string,cha):
    count = 0 
    for c in string:
        if ord(c) == ord(cha):
            count+=1
    
    return count


if __name__ == "__main__":
    string = input("Enter the string: ")
    cha = input("Enter the character whose occurrence count is required: ")

    charOccurrence = count_occurrence(string,cha)

    print('Number of time character \"',cha,'\" appreared in string \"',string, '\" is: ', charOccurrence,'.')