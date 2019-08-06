import sys
import calcy

#shopping
veg,fruits,cash = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
total_cost=calcy.add(veg,fruits)
cash_return=calcy.sub(cash,total_cost)
print("cash to be returned is :",cash_return)
