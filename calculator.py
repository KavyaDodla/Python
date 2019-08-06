def add(num1,num2):
    res=num1+num2
    return res

def sub(num1,num2):
    res=num1-num2
    return res

#Main
first = 10
second = 20
total = add(first, second)
print("Sum:", total)
difference = sub(first, second)
print("Difference:", difference)

#test match
england1 = 250
india1 = 220
england2 = 180
england_total=add(england1, england2)
score_diff=sub(england_total, india1)
runs_required=add(score_diff, 1)
print("runs required to win is:",runs_required)

#shopping
veg = 120
fruits = 45
cash = 200
total_cost=add(veg,fruits)
cash_return=sub(cash,total_cost)
print("cash to be returned is :",cash_return)





