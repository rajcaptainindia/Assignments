#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=("Veg Roll", "Noodles", "Fried Rice" , "Soup")
quantity_available=[2,200,3,0]
'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    
    for elem in item_tuple:
        end_of_current_item=False
        if not str(elem).isnumeric():
            #print(elem)
            if elem not in menu:
                print(elem,"is not available")
            else:
                item=menu.index(elem)
        else:
            quantity=elem
            end_of_current_item=True
        if end_of_current_item:
            #print(item,quantity)
            check_quantity_available(item,quantity)
                
    #Remove pass and write your logic here


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index] - quantity_requested < 0):
        print(menu[index],"stock is over")
    else:
        print(menu[index],"is available")
        updated_quantity=  quantity_available[index] - quantity_requested
        quantity_available[index]= updated_quantity
        
        
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
place_order("Fried Rice",2,"Soup",1)
