
"""
Ask the user to enter a 3 digit number till he enters 0
              Print the square root of only 3 digit positive numbers.
              Make sure that the program does not print the square root of any number that is not a 3 digit number
"""
import math

def prompt():
    """
    input:Get input from user untill he enters 0 and store the numbers in a list
    return list

    """
    number=int(input("Please enter a 3 digit number"))
    list=[]
    while number!=0:
        list.append(number)
        number=int(input("please enter a least positive digit"))
        continue
    return list

def three_digit():
    """
    input: list from prompt()
    output:square root of 3 digit numbers form list
    :return:
    """
    list=prompt()
    three_digit_positive=[]
    for i in list:
        if i>99 and i<1000:
            a=math.sqrt(i)
            three_digit_positive.append(a)
    for i in three_digit_positive:
        print(i)
#main starts here
three_digit()











