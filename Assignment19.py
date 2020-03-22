#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if((food_type=="N" or food_type=="V") and quantity_ordered>0 and distance_in_kms>0):
        delivery_charge=0
        rate=0
        for i in range(1,distance_in_kms+1):
            if(i<=3):
                rate=0
            elif(i>3 and i<=6):
                rate=3
            else:
                rate=6
            delivery_charge=delivery_charge+rate
        if(food_type=="N"):
            bill_amount=delivery_charge+quantity_ordered*150
        else:
            bill_amount=delivery_charge+quantity_ordered*120
    else:
        bill_amount=-1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
