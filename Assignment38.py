#PF-Assgn-38

def check_double(number):
    #pass
    #Remove pass and write your logic here
    digits=len(str(2*number))
    for num in str(number):
        if num not in str(2*number):
            return False
    return True
#Provide different values for number and test your program
print(check_double(125874))
