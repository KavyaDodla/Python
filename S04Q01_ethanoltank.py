"""
When the tank is more than 80% full, it should raise an alarm to close the valve
When the tank is less than 20% full, it should send an SMS to buy more liquid.
"""
def prompt_user():
    """
    Input:user enter data for tank capacity and ethanol level
    output:fill rate
    return fill rate
    """
    tank_capacity=int(input("What is the total tank capacity"))
    ethanol_level=int(input("Please enter the reading of ethanol in tank"))
    fill_rate=(ethanol_level*100)/tank_capacity
    return fill_rate

def tank_check():
    """
    input: fill rate from prompt_user function
    out put: print statement-When the tank is more than 80% full, it should raise an alarm to close the valve.
    When the tank is less than 20% full, it should send an SMS to buy more liquid.

    """
    percentage=prompt_user()
    if percentage>80:
        print("Your tank is",percentage,"full. Please close the valve")
    elif percentage<20:
        print("Your tank is", percentage, "Please send ans SMS to user to buy more liquid")
# main starts from here
tank_check()

