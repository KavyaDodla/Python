"""
Take a number as input from the user.
           Print all the squares of numbers from 1 to any large number.
           The numbers printed should be less than
                 the number given as input by the user
"""
def user_input():
    """
    Input: User enters a number
    Store it in list taking input as range
    :return:  user entered number and list
    """
    
    number=int(input("Please enter a number"))
    list=range(number)
    return number,list

def logic():
    """
    Assaign values for user_input function to variables
    create of list of suqares till they are less than user input
    out put: square_list
    """
    user_number,list=user_input()
    square_list=[]
    for i in list:
        square=i*i
        if square<user_number:
            square_list.append(square)
    print("The squares of numbers till the input were:",square_list)

#main starts here
logic()
