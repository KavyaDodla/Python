start=0
end=int(input("What is the end reading seen in odometer in terms of kilometers"))
fueltank_capacity=100
fuel_reading=int(input("What is the current fuel reading seen now in terms of litres"))
fuel_consumed=fueltank_capacity-fuel_reading
def mileage_calculator():
    mileage = int((end - start) / fuel_consumed)
    #print (mileage, "kms/lt")
    return mileage
mileage1=mileage_calculator()
def refilling():
    distance=560
    fuel=distance/mileage1
    stops=int(fuel/fueltank_capacity)
    print(" Number of stops required to refill the tank by the time you reach goa is",stops)
mileage_calculator()
refilling()

