#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    sum=0
    count=0
    num_list.sort()
    #pass
    #Remove pass and write your logic here
    for num in num_list:
        if(num<n):
            sum+=num
            if(sum<=n):
                count+=1
    if(count!=0):
        return count
    else:
        return -1 

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
