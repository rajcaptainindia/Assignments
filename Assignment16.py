#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    extra_one_needed=0
    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make%5
    if(no_of_five<five_needed):
        one_needed=one_needed+((five_needed - no_of_five)*5)
        five_needed=no_of_five
    
    if(5*no_of_five+(no_of_one)>=rupees_to_make and no_of_one>=one_needed):
        
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,20,5)
