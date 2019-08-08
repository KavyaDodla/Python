"""
Print out forst 10 fibonacci numbers
"""
def logic():
    a=1
    b=1
    counter=0
    position = int(input("Please enter how many fibonacci numbers you require"))
    repeat=((position-2)/2) # since a and b are defined at first,if user wants 10 fibonacci numbers we only require 8 more.Each time we get two numbers.so it would be half of 8
    print("", a , "\n" , b)
    while counter<(repeat):
        a=a+b
        b=a+b
        counter=counter+1
        print("", a, "\n", b)
# main starts here
logic()




