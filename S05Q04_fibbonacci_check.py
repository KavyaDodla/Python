"""
Check if a given number is a fibonacci number.
           If not, then print the closest fibonacci number to the given number
"""

def fibbonacci():
    user_number=int(input("Please enter an number"))
    fibbonacci_list=[1,1]
    a = 1
    b = 1
    while fibbonacci_list[-1]<user_number:
        res = a + b
        a = b
        b = res
        fibbonacci_list.append(b)
    return fibbonacci_list,user_number

def check():
    
    list,number=fibbonacci()
    if list[-1]==number:
        print(" Your input:",number,"is fibonacci number")
    elif list[-1]!=number:
        diff1=list[-1]-number
        diff2=list[-2]-number
        if diff1>0 and diff2>0:
            if diff1>diff2:
                print("The nearest fibonacci number is",list[-2])
            else:
                print("The nearest fibonacci number is",list[-1])
        elif diff1<0:
            diff_1=-(diff1)
            if diff1 > diff2:
                print("The nearest fibonacci number is",list[-2])
            else:
                print("The nearest fibonacci number is", list[-1])
        else:
            diff_2=-(diff2)
            if diff1 > diff2:
                print("The nearest fibonacci number is", list[-2])
            else:
                print("The nearest fibonacci number is", list[-1])

#fibbonacci()
check()



