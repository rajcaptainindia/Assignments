#PF-Assgn-29
def calculate(distance,no_of_passengers):
    #pass
    #Remove pass and write your logic here
    price_per_km= 7
    actual_price=distance*price_per_km
    profit_price=80*no_of_passengers
    if(actual_price>profit_price):
        return -1
    else:
        return profit_price - actual_price
#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
