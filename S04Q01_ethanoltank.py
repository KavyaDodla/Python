def get_data():
    tank_capacity=int(input("please enter the total tank capacity"))
    current_capacity=int(input(" Please enter the curent level of ethanol in the tank"))
    return tank_capacity,current_capacity
    
def alarm(percentage):
    print ("Please close the valve.Your tank is ",percentage,"full")

def sms(percentage):
    print("Please buy more ethanol. Your ethanol percenatage is",percentage)

def check_percentage():
    tank_capacity,current_capacity=get_data()
    percentage=(current_capacity*100)/tank_capacity
    if percentage>=80:
        alarm(percentage)
    elif percentage<=20:
        sms(percentage)
    
def main():
    check_percentage()
    
main()
    


    

    
