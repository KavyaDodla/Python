def get_data():
    number=(input("Please enter the number->"))
    return number
def logic():
    number=get_data()
    length=len(number)
    for i in number:
        if i==".":
            length=length-1

    if length==1:
        number=int(number)
        number=number+7
        units=number%10
        print("The units place for single digit number entered after summing with 7 is is ->",units)
    elif length==2:
        number=int(number)
        number=number**5
        number=str(number)
        print("The last two digits of entered 2 digit number after raising 5 times are->",number[-2:])
    elif length==3:
        number2=int(number)
        number=int(get_data())
        final=number2+number
        final=str(final)
        print("The last three digits of sum of your previous 2 entries are->",final[-3:])

logic()



