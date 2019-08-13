"""
Ask the user to enter a number till he enters 0.
          Print the maximum and minimum values among all entered numbers.
          Print the number of single, two and three digit numbers entered.
"""


def number():
    """
    Taking input from user and creating a list of numbers
    Input:user input
    Output: we will return list generated as "number"
    :return:
    """
    user_number =int(input("Please enter an number"))
    number = []
    while user_number!=0:
        number.append(user_number)
        print(number)
        user_number=int(input("Please enter least positive integer"))
        continue
    return number


def min_max():
    """
    Input: We will cal function number() to get returned value frm  it to list
    Excute the logic for mac and minimum out of list
    Out put: we print max and minimum numbers
    Return list 
    """
    list=number()
    max=0
    min=list[0]
    for i in list:
        if i>max:
            max=i
            for i in list:
                if i<min:
                    min=i
    print("Maximum number you entered is:",max)
    print("Minimum number you entered is :",min)
    return list

def digits():
    """
    input: min_max return list
    we execute logic for single,double and triple digitd by using counter
    out put: print number of single digits entered,two digits entered,3 digits entered

    """
    list=min_max()
    print(list)
    single_counter=0
    double_counter=0
    triple_counter=0
    for i in list:
        if i>-10 and i<10:
            single_counter=single_counter+1
        elif i>-100 and i<-9 or i<100 and i>9:
            double_counter=double_counter+1
        elif i>-1000 and i<-99 or i>99 and i<1000:
            triple_counter=triple_counter+1
    print("You have entered", single_counter ,"single digit numbers and",double_counter,"two digit numbers and",triple_counter,"three digit numbers" )
#main starts here
digits()




