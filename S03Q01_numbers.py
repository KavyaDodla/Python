"""
Take 2 numbers from the user.
            Print which number is a 2 digit number,
            and which number is a 3 digit number.
            If it is neither, then print the number as it is
"""
def prompt():
    """
    Prompt user for input for 2 numbers
    :return: number1 and number 2
    """
    number1,number2=int(input("Please type first number")), int(input("Please type second number"))
    return number1,number2
def print_number():
    """
    input: return prompt()number1 and number 2
    count is set as 0 so that we can use it to print which number we are checking
    out put: print statement
    :return: 
    """
    num=prompt()
    count = 0
    for i in num:
        count=count+1
        if i>9 and i<100:
            print("Your", count , "number is a two digit numer:",i)
        elif i>99 and i<1000:
            print("Your", count, "number is a three digit number:",i)
        else:
            print("Your", count, "number is neither two digit nor three digit:",i)
# main stars here
print_number()


