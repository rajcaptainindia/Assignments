#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    numlist=[]
    # Write your logic here
    #return max_num
    if(num1<num2):
        for i in range(num1,num2+1):
            if(len(str(i))==2):
                if(i%5==0):
                    if(((i%10)+(i//10))%3==0):
                        numlist.append(i)
        if(len(numlist)>0):
            return max(numlist)
        else:
            return max_num
    else:
        return max_num
#Provide different values for num1 and num2 and test your program.
max_num=find_max(1,99)
print(max_num)
