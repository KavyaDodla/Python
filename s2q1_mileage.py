# i will need fuel tank capacity and fuel reading info to calculate mileage.
start=0
end=int(input("What is the end reading seen in odometer in terms of kilometers"))
fueltank_capacity=50
fuel_reading=int(input("What is the current fuel reading seen now in terms of litres"))
fuel_consumed=fueltank_capacity-fuel_reading
mileage=(end-start)/fuel_consumed
print (mileage,"kms/lt")
