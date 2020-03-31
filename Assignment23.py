#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for gem in reqd_gems:
        if(gem not in gems_list):
            return -1
        else:
            index_of_gem=gems_list.index(gem)
            bill_amount=bill_amount+(price_list[index_of_gem]*reqd_quantity[reqd_gems.index(gem)])
    if(bill_amount>30000):
        bill_amount=bill_amount-bill_amount*(5/100)
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
