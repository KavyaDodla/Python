
import random


def pass_code():
    code=range(1,26)
    employee_code=random.choice(code)
    return employee_code

def output():
    print("Hi welcome to the census tool box")
    employee_code=pass_code()
    user_input = int(input("Enter the passcode"))

    counter=0
    repeat = 0
    while counter<3:
        if user_input==employee_code:
            print("Welcome")
            break
        elif (user_input+2)<employee_code:
            print("invalid passcode")
            user_input=user_input = int(input("Enter the passcode"))
            counter=counter+1

        elif (user_input-2)>employee_code:
            print("INVALID PASSCODE")
            user_input = int(input("Enter the passcode"))
            counter = counter + 1

        else:
            print("InVaLiD PaSsCoDe")
            if repeat<2:
                counter = counter
                repeat=repeat+1
                user_input = int(input("Enter the passcode "))
            else:
                counter = counter + 1
                user_input = int(input("Enter the passcode"))

    else:

        print("LOG IN FAILED")

# main starts from here
output()















