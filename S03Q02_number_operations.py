"""
number is a single digit add 7 to it and print the number in its units place
If number is two digit,raise it to the power of five
If number is three digit request for another number and add them both
"""


def prompt():
    """
    prompt user to give a number and return it
    :return:
    """
    number=int(input("Please enter a number"))
    return number

def one_digit(num):
    """
    input:number from finalcheck
    out put: add 7 to number and print the units place of result

    :param num:
    """
    result=str(num+7)
    print (result[-1])

def two_digit(num):
    """
    input:number from finalcheck
    out put: raise it to the power of 5. print the units place of result
    :param num:
    """
    result=str(num**5)
    print(result[-1])

def three_digit(num):
    """
    input:number from final check
    out put: request other number and add them both.Print units place of result
    :param num:
    """
    num1=int(input("Give me one more number"))
    result=str(num+num1)
    print(result[-1])

def final_check():
    num=prompt()
    if num >= 0 and num < 10:
        one_digit(num)
    elif num>=10 and num<100:
        two_digit(num)
    elif num>=100 and num<1000:
        three_digit(num)

# main starts here
final_check()


