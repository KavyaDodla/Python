def add(num1,num2):
    res=num1+num2
    return res

def sub(num1,num2):
    res=num1-num2
    return res

#Main
if __name__=="__main__":
    first = 10
    second = 20
    total = add(first, second)
    print("Sum:", total)
    difference = sub(first, second)
    print("Difference:", difference)
