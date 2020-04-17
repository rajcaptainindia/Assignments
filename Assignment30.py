#PF-Assgn-30

def encode(message):
    message=message+" "
    res=""
    count=1
    ch=""
    for i in range(0,len(message)-1):
        ch=message[i]
        if(message[i] == message[i+1]):
            count+=1
        else:
            res+=str(count)+ch
            count=1
    return res
            
            
        
            
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
