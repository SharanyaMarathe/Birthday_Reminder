import datetime

def Current_Date():
	#print("Inside Current")
	Today=datetime.date.today()  #To get current date and day
	Today_day=Today.strftime("%A")
	return Today,Today_day


def Birthday(date):
	#print("Inside Birthday")
	#date=input("Input Your Birth date in dd-mm-yy format: ")
	date_l=date.split("-")
	d1=datetime.date(int(2020),int(date_l[1]),int(date_l[0]))
	p= "On "+d1.strftime("%A") +", "+date_l[0]+"th "+d1.strftime("%B") #To notify the user birthday details of year 2020
	return d1,p


def Notification(c,b):
	#print("Inside Notify")
	
	if(c.month == b.month):
		return ( "In same month")

	elif((b.month - c.month) > 0):
		return  (str(b.month - c.month)+"Months from now")

	else: 
		return (str(c.month - b.month) +"Months Ago")


def Display_Notifications(date):
	#print("Inside Display")
	Current_Info=Current_Date()
	
	Birthday_info=Birthday(date)
	notes=Notification(Current_Info[0],Birthday_info[0])
	print(str(Current_Info)," || ",Birthday_info[1]," || ",notes)



# input is taken from the user only this file is run directly	
if __name__ =="__main__" :
	date=input("Input Your Birth date in dd-mm-yy format: ")
	dsn=Display_Notifications(date)




