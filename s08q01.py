def logic():
    number=(input("Please enter the number->"))
    length=len(number)
    for i in number:
        if i==".":
            length=length-1
    print("The number of digits in the given number is->",length)
logic()



