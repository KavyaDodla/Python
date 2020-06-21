import sys

def max_number(FH):
    numbers=FH.read().splitlines()
    print(numbers)
    x=0
    count=0
    for i in numbers:
        count+=1
        y=int(i)
        if y>x:
            x=y
    print("The maximum number in the file is ->",x)
    return numbers

def sum_numbers(FH,numbers):
    x=0
    for i in numbers:
        y=int(i)
        x=x+y
    print("The sum of numbers is->",x)

def main():
    file=sys.argv[1]
    with open(file,'r') as FH:
        numbers=max_number(FH)
        sum_numbers(FH,numbers)

if __name__=="__main__":
    main()


S11Q01.py
