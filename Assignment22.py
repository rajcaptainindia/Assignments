#PF-Assgn-22
def find_leap_years(given_year):
    temp_year=given_year
    is_leap_year=False
    list_of_leap_years=[]
    while(is_leap_year!=True):
        if(given_year%4==0):
            if(given_year%100==0):
                if(given_year%400==0):
                    is_leap_year=True
                else:
                    is_leap_year=False
            is_leap_year=True
        else:
            is_leap_year=False
        if(is_leap_year==True):
            given_year=given_year
        else:
            given_year=given_year+1       
    # Write your logic here
    if(temp_year==given_year):
        given_year=given_year+4
    list_of_leap_years.append(given_year)
    next_year=given_year
    for i in range(14):
        next_year=next_year+4
        list_of_leap_years.append(next_year)
        next_year
    return list_of_leap_years
    
list_of_leap_years=find_leap_years(2019)
print(list_of_leap_years)
