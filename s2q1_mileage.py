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
# main starts from here
mileage()
