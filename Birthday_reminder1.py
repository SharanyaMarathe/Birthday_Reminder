import datetime

def Current_Date():
	print("Inside Current")
	Today=datetime.date.today()  #To get current date and day
	Today_day=Today.strftime("%A")
	return Today,Today_day


def Birthday(date):
	print("Inside Birthday")
	#date=input("Input Your Birth date in dd-mm-yy format: ")
	date_l=date.split("-")
	d1=datetime.date(int(2020),int(date_l[1]),int(date_l[0]))
	p= "On "+d1.strftime("%A") +", "+date_l[0]+"th "+d1.strftime("%B") #To notify the user birthday details of year 2020
	return d1,p


class Notification():
	print("Inside Notify")
	Current_Info=Current_Date()
	date=input("Input Your Birth date in dd-mm-yy format: ")
	Birthday_info=Birthday(date)
	c=Current_Info[0]
	b=Birthday_info[0]
	if(c.month == b.month):
		result= "In same month"

	elif((b.month - c.month) > 0):
		result= str(b.month - c.month)+"Months from now"

	else: 
		result= str(c.month - b.month) +"Months Ago"


class Display_Notifications(Notification):
	print("Inside Display")
	notes=Notification()
	print(str(notes.Current_Info)," || ",notes.Birthday_info[1]," || ",notes.result)




dsn=Display_Notifications()


#Current_Info=Current_Date()
#Birthday_info=Birthday()
#print("Date"+" || ","Day"+" || "+"Detail")
#print(Current_Info," || ",Birthday_info[1])
#notes=Notification(Current_Info[0],Birthday_info[0])
#notes=Notification()
#print(Current_Info," || ",Birthday_info[1]," || ",notes)
