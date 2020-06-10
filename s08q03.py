# S08Q03
# Ask the user to enter a number.
# - If the user enters a number as 5, then
# generate the following string :
# - 00001111222233334444
#
# - If the user enters the number as 3, then
# generate the following string :
# - 001122
def get_data():
    number=int(input("Please choose the number between 5 or 3->)"))
    return number
def main():
    number=get_data()
    word=[]
    if number==5:
        for i in range(0,5):
            i=str(i)
            output=i*4
            word.append(output)
    elif number==3:
        for i in range(0,3):
            i=str(i)
            output=i*2
            word.append(output)
    print("".join(word))
main()



