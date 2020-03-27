#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    next_day=day
    next_month=month
    next_year=year
    leapyear=0
    days_in_month=0
            #checking leapyear
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                leapyear=1
            else:
                leapyear=0
        leapyear=1
    else:
        leapyear=0
        # feb month should have either 28 or 29 day only 
    if(leapyear==0 and month==2 and day>28):
        print("Invalid Date")
        return
    elif(leapyear==1 and month==2 and day>29):
        print("Invalid Date")
        return
        #end of leapyear logic
        #actual logic
    if(day>0 and day<=31 and month>0 and month<=12):
        #months logic
        if month in (1,3,5,7,8,10,12):
            days_in_month=31
        elif(month==2):
            if(leapyear==1):
                days_in_month=29
            else:
                days_in_month=28
        else:
            days_in_month=30
        #end of months logic
        if(day<days_in_month):
            next_day+=1
            next_month=month
        else:
            next_day=1
            if(month==12):
                next_month=1
                next_year=year+1
            else:
                next_month=month+1
        
    else:
        print("Invalid Date")
        return
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,2,2020)

