# this is the program for sumops.py
#commiting both programs code in this commit
import sys

def dsum():
    number=sys.argv[1]
    sum=0
    for i in number:
        sum=sum+int(i)
    print("The sum of digits for entered number is :",sum)
    return sum

if __name__=="__main__":
    dsum()

# this  is the progrma for jackpot .py
import sys
from S0BQ03 import dsum
from random import randint

def get_number():
    if len(sys.argv)==1:
        number=int(input("Please enter the 5 digit number->"))
    else:
        number=sys.argv[1]
        print(number)
        return number

def winner(sum,number):
    random_number=randint(1,50)
    if sum==random_number:
        print("Congrats you won the jackpot!!!",number)
    else:
        print("Better lucknext time:",random_number)




def main():
    number=get_number()
    sum=dsum()
    winner(sum,number)

main()


