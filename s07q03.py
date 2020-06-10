def get_data():
    sentence=input("Please enter the sentence")
    return sentence


def character():
    sentence=get_data()
    print("The last character in a sentence is->",sentence[-1])
    print("The last 5 characters in a sentence is->",sentence[-5:]) 
    print("The second character in a sentence is->",sentence[1], "the 5th character in a sentence is->",sentence[4])
    length=len(sentence)
    y=(int(length/2)-1)
    print("The character at the center of the string with adjoing characters is->",sentence[y-1],sentence[y],sentence[y+1])

character()
