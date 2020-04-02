import datetime
date=input("Input Your Birth date in dd-mm-yy format: ")
Today=datetime.date.today()  #To get current date and day
Today_day=Today.strftime("%A")
#print("TODAY'S Day: ",Today_day)
date_l=date.split("-")
d1=datetime.date(int(2020),int(date_l[1]),int(date_l[0])) #To compare at last
p= "On "+d1.strftime("%A") +", "+date_l[0]+"th "+d1.strftime("%B") #To notify the user birthday details of year 2020
print("Date"+" || ","Day"+" || "+"Detail")
print(Today," || ",Today_day," || ",p )
'''print("First day of the week is--->",d.strftime("%A"))
month_days={1:["jan",31],2:["Feb",28],3:["Mar",31],4:["Apr",30],5:["May",31],6:["June",30],7:["July",31]
            ,8:["Aug",31],9:["Sept",30],10:["Oct",31],11:["Nov",30],12:["Dec",31]}
if((int(date_l[2])%4==0) or (int(date_l[2])%100==0) or (int(date_l[2])%400==0) or int(date_l[1])==2):
    print("This is a leap year and this month has 29 days")
else:
    print("This month is ",d1.strftime("%B"),"It has",month_days[int(date_l[1])][1],"days")'''
