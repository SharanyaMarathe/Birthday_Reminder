import datetime

def Current_Date():
	
	Today=datetime.date.today()  #To get current date and day
	Today_day=Today.strftime("%A")
	return Today,Today_day


def Birthday(date):
	
	date_l=date.split("-")
	d1=datetime.date(int(2020),int(date_l[1]),int(date_l[0]))
	p= "On "+d1.strftime("%A") +", "+date_l[0]+"th "+d1.strftime("%B") #To notify the user birthday details of year 2020
	return d1,p


def Notification(c,b):
	
	if(c.month == b.month):
		return ( "In same month")

	elif((b.month - c.month) > 0):
		return  (str(b.month - c.month)+"Months from now")

	else: 
		return (str(c.month - b.month) +"Months Ago")


def Display_Notifications(date):
	
	Current_Info=Current_Date()
	Birthday_info=Birthday(date)
	notes=Notification(Current_Info[0],Birthday_info[0])
	return str(notes)



if (__name__ == "__main__") :
	date=input("Input Your Birth date in dd-mm-yy format: ")
	dsn=Display_Notifications(date)




