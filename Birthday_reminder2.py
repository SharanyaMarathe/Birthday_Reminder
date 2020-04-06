import datetime

def Current_Date(date):
	print("Inside Current")
	Today=date.split("-")  #To get current date and day
	Today_detail=datetime.date(int(Today[2]),int(Today[1]),int(Today[0]))
	Today_day=Today_detail.strftime("%A")
	return Today_detail,Today_day


def Birthday():
	
	Birth_date= "15-03-1995"
	print("Birthday date is: ",Birth_date)
	date_l=Birth_date.split("-")
	d1=datetime.date(int(2020),int(date_l[1]),int(date_l[0]))
	p= "On "+d1.strftime("%A") +", "+date_l[0]+"th "+d1.strftime("%B") #To notify the user birthday details of year 2020
	return d1,p


def Notification(c,b):
	print("Inside Notify")
	
	if(c.month == b.month):
		if(c.day > b.day):
			if((c.day-b.day)%7 ==0):
				return ((str(c.day - b.day)/7)+ "weeks ago")
			else:
				return (str(b.day - c.day)+ "days ago")
		elif(b.day > c.day):
			if((b.day-c.day)%7 ==0):
				return ((str(b.day - c.day)/7)+ "weeks from now")
			else:
				return (str(b.day - c.day)+ "days from now")
		else:
			return ("Today")

	elif((b.month - c.month) > 0):
		if(b.month - c.month ==1):
			return ("Next Month")
		else:
			return  (str(b.month - c.month)+"Months from now")

	else: 
		if(c.month - b.month ==1):
			return ("Last Month")
		else:
			return (str(c.month - b.month) +"Months Ago")


def Display_Notifications(date):
	print("Inside Display")
	Current_Info=Current_Date(date)
	Birthday_info=Birthday()
	notes=Notification(Current_Info[0],Birthday_info[0])
	print(str(Current_Info)," || ",Birthday_info[1]," || ",str(notes))
	#return str(notes)



if (__name__ == "__main__") :
	date=input("Input Your Current date in dd-mm-yy format(To get relavemt notification): ")
	dsn=Display_Notifications(date)



