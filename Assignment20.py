#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    temp=account_number
    no_of_digits=0
    while(temp>0):
        temp=temp//10
        no_of_digits+=1
    first_digit=account_number//1000
    if(first_digit==1 and no_of_digits==4):
        if(account_balance>=100000):
            if(loan_type=="Car" and salary>25000):
                eligible_loan_amount=500000
                bank_emi_expected=36
            elif(loan_type=="House" and salary>50000):
                eligible_loan_amount=6000000
                bank_emi_expected=60
            elif(loan_type=="Business" and salary>75000):
                eligible_loan_amount=7500000
                bank_emi_expected=84
            else:
                print("Invalid loan type or salary")
                return
        else:
            print("Insufficient account balance")
            return
    else:
        print("Invalid account number")
        return
    if(loan_amount_expected>eligible_loan_amount or customer_emi_expected>bank_emi_expected):
        print("The customer is not eligible for the loan")
        return
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:",customer_emi_expected)

calculate_loan(1001,40000,250000,"Car",300000,30)
