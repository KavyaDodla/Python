"""
print the multiplication table of any number desired by the user
"""

def multiplication_table(a):
    """
    param required:a
    use for loop to print out first 10 multiplication results
    """
    for i in range(1,11):
        b = a * i
        print(a, "*" , i , "=" , b)

def number():
    """
    get number for which multiplication table needs to be printed
    input:user input
    convert input to integer
    execute program only if input is more than 0.return value of user input
    output:return user input
    """
    a=int(input("Please enter the number for multiplication table"))
    if a>0:
        return a
    else:
        print("Please enter valid input")

def main():
    a=number()
    multiplication_table(a)
#main starts here
main()






