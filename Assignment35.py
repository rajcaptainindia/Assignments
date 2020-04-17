#PF-Assgn-35
################################ one test case failed
#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #pass
    #Remove pass and write your logic here
    avg=sum(list_of_marks)/len(list_of_marks)
    count=0
    for i in list_of_marks:
        if(i>avg):
            count+=1
    return count*10

def sort_marks():
    #pass
    #Remove pass and write your logic here
    res= list(list_of_marks)
    res.sort()
    return res

def generate_frequency():
    res=[0]*(max(list_of_marks)+1)
    for i in range(len(list_of_marks)):
        count=list_of_marks.count(list_of_marks[i])
        index= list_of_marks[i]
        if(count>0):
            res[index]=count
    return res
            
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
