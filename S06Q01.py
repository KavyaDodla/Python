"""Write a program that takes multiple sentences as input from the user.
          The last input is indicated by an empty line.
          - Find the number of words entered
          - Find the number of words that contain the vowel ‘a’"""
def data():
    lines=[]
    while True:
        line=input(">")
        if line:
            lines.append(line)
        else:
            break
    text= '\n'.join(lines)
    words=text.split()
    return words

def output():
    words=data()
    print("You entered",len(words),"words")
    vowel_list=[]
    for word in words:
        for letter in word:
            if letter=="a":
                vowel_list.append(word)
                break
    print(len(vowel_list),"words contain letter a")

def main():
    output()


#main starts here
main()
