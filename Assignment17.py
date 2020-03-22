#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    new_salary=current_salary
    if(job_level==3):
        new_salary=(current_salary+(current_salary*15)/100)
    elif(job_level==4):
        new_salary=(current_salary+(current_salary*7)/100)
    elif(job_level==5):
        new_salary=(current_salary+(current_salary*5)/100)
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,6)
print(new_salary)
