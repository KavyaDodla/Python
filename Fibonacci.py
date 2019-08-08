"""
Based on the user input print either even or odd or all fibonacci numbers
"""
def fib(fib_count):
    """
    input:count
    :param fib_count:
    :return:
    """
    a = 1
    b = 1
    fib=[1,1]
    counter=0
    while fib.__len__()<fib_count:
        res = a+b
        a=b
        b=res
        fib.append(res)

    print("All Fibonacci numbers : ")
    for f in fib:
        print(f)

def fib_even(fib_type, fib_count):
    print("inside")

    a = 1
    b = 1
    fib=[]
    counter=0
    while fib.__len__()<fib_count:
        res = a+b
        a=b
        b=res
        if fib_type == "even":
            if res % 2 == 0:
                fib.append(res)

    print("Even Fibonacci numbers : ")
    for f in fib:
        if f % 2 == 0:
            print(f)


def fib_odd(fib_type, fib_count):
    print("inside")

    a = 1
    b = 1
    fib=[]
    counter=0
    while fib.__len__()<fib_count:
        res = a+b
        a=b
        b=res
        if fib_type == "odd":
            if res % 2 != 0:
                fib.append(res)
    print("Odd Fibonacci numbers : ")
    for f in fib:
        if f % 2 != 0:
            print(f)

def main():
    fib_type=str(input("Even/Odd/all fibonnaci numbers you need?"))
    fib_count = int(input("How many " + fib_type + " numbers you need?"))
    if fib_type == "even":
        fib_even(fib_type, fib_count)
    elif fib_type == "odd":
        fib_even(fib_type, fib_count)
    else:
        fib(fib_count)

main()


# def fib(fib_type, fib_count):
#     print("inside")
#
#     a = 1
#     b = 1
#     fib=[]
#     counter=0
#     while fib.__len__()<fib_count:
#         res = a+b
#         a=b
#         b=res
#         if fib_type == "even":
#             if res % 2 == 0:
#                 fib.append(res)
#         if fib_type == "odd":
#             if res % 2 != 0:
#                 fib.append(res)
#
#     if fib_type == "even":
#         print("Even Fibonacci numbers : ")
#         for f in fib:
#             if f % 2 == 0:
#                 print(f)
#     elif fib_type == "odd":
#         print("Odd Fibonacci numbers : ")
#         for f in fib:
#             if f % 2 != 0:
#                 print(f)
