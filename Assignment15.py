def solution(num1,num2,num3):
    if(num3==7):
        return -1
    elif(num2==7):
        return num3
    elif(num1==7):
        return num1*num2
    else:
        return num1*num2*num3
n1=(int)(input("Enter 1st number: "))
n2=(int)(input("Enter 2rd number: "))
n3=(int)(input("Enter 3rd number: "))
print("Output is : {}".format(solution(n1, n2, n3)))
