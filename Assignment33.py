#PF-Assgn-33

def find_common_characters(msg1,msg2):
    #pass #Remove pass and write your logic here
    res=""
    for chr in msg1:
        if(chr in msg2):
            if(chr!= " "):
                res+=chr
    if(len(res)>0):
        return res.strip() 
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
        
common_characters=find_common_characters(msg1,msg2)
print(common_characters) 
