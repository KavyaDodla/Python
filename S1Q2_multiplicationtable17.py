"""
print multiplication table 17
"""
def multiplication_table():
    """
    Using for loop to print multiplication table till 10
    Input: 17
    """
    a=17
    for i in range(1,11):
        b=a*i
        print(a, "*" , i , "=" , b)
#main starts here
multiplication_table()




