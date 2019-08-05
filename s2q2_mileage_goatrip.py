"""
mileage calculation
"""

def readings():
    """
    prompt users to give details of start and end points of ododmeter
    tank capacity of vehicle,current tank reading

    :return:
    """
    start = int(input("What is the start reading seen in odometer in terms of kilometers"))
    end = int(input("What is the end reading seen in odometer in terms of kilometers"))
    tank_capacity = int(input("what is the tank capacity of your vehicle"))
    fuel_reading = int(input("What is the current fuel reading seen now in terms of litres"))
    return start,end,tank_capacity,fuel_reading

def mileage():
    """
    input: cal function readings and use the return values from readings to calculate mileage

    """
    start_reading, end_reading, fueltank_capacity, currentfuel_reading=readings()
    fuel_consumed=fueltank_capacity-currentfuel_reading
    mileage=(end_reading-start_reading)/fuel_consumed
    print (mileage,"kms/lt")
    return mileage,fueltank_capacity

def refilling():
    """
    input: cal function mileage, use values returned(mileage and fuel tank capacity) from it
    calculate stops
    print the out put
    :return:
    """
    mileage1,tank_capacity = mileage()
    distance=560
    fuel=distance/mileage1
    stops=int(fuel/tank_capacity)
    print(" Number of stops required to refill the tank by the time you reach goa is",stops)

#main starts from here
refilling()


