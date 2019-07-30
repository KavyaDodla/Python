def multiplication_table(a):
    for i in range(1, 11):
        b = a * i
        print(a, "*", i, "=", b)
a=(input)("What is the number you wish to see multiplication table for?")
a=int(a)
if a>0:
    multiplication_table(a)
else:
    print("Please enter valid input")
