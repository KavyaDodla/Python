def file_name():
    filename=input("Please enter the file name that you need check tob be performed")
    return filename
def uppercase_check(FH):
    fullfile=FH.read()
    print(fullfile)
    sentences=fullfile.split(".")
    print(sentences)
    count=0
    for i in sentences:
        count=count+1
        if i[0]=="\n":
            character=i[1]
            if character.isupper()==True:
                print(("The first character in sentence"),count,"is in upper case ->",character)
            else:
                print(("The first character in sentence"),count,"is in lower case->",character)
        else:
            character=i[0]

            if character.isupper()==True:
                print(("The first character in sentence"),count,"is in upper case ->",character)
            else:
                print(("The first character in sentence"),count,"is in lower case->",character)




def main():
    filename=file_name()
    with open(filename,'r') as FH:
        uppercase_check(FH)

if __name__=="__main__":
    main()



