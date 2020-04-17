#PF-Assgn-36
def create_largest_number(number_list):
    res=''
    #remove pass and write your logic here
    while(len(number_list)!=0):
        res+=str(max(number_list))
        number_list.remove(max(number_list))
    return int(res)
        

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
