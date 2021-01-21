import sqlite3
import os
from termcolor import colored
import os
os.system('color')

# To connect database
def initial():
	#check database file
	if os.path.isfile('subject_list.db'):
		pass
	else:
		conn = sqlite3.connect('user_database.db')

	#connect database and make object
	conn = sqlite3.connect('user_database.db')

	#make a cursor to navigate
	c = conn.cursor()

	return [c,conn]   

# To initialize database and tables in it
def initialize_table():
	infin = initial()
	c = infin[0]
	conn = infin[1]

	#create subject_list table in database
	c.execute("CREATE TABLE IF NOT EXISTS subject_list (subject TEXT, link TEXT)")

	#create timetable table in database
	i = 0
	lst = ["Mon","Tue","Wed","Thus","Fri","Sat","Sun"]
	for i in range(0,7):	
		st = "CREATE TABLE IF NOT EXISTS "+lst[i]+" (lectureNo INT,subject TEXT, time TEXT)"
		c.execute(st)


# To insert Time table	
def insertinto_timetable():
	i = 0
	lst = ["Mon","Tue","Wed","Thus","Fri","Sat","Sun"]
	infin = initial()
	c = infin[0]
	conn = infin[1]
	while i<=6 : 
		if input("Do you want to insert for "+lst[i]+" (y/n) :") == "y" :
			#st = "DROP TABLE IF EXISTS "+lst[i]
			#c.execute(st)
			st = "CREATE TABLE IF NOT EXISTS "+lst[i]+" (lectureNo INT,subject TEXT, time TEXT)"
			c.execute(st)
			lectureno = input(colored("Input Lecture No: ",'green'))
			subject = input(colored("Input Subject: ",'green'))
			time = input(colored("Time: ",'green'))
			#time = input("Input Time In 'HH:MM' 24hours Format: ")
			st = "INSERT INTO "+lst[i]+" (lectureNo,subject,time) VALUES(?, ?, ?)"
			c.execute(st,(lectureno, subject, time))
			conn.commit()

			display_timetable(lst[i])
			print("\n")
		else:
			i+=1
			
#To insert subject and link for the meeting
def insertinto_subject_list():
	while True :
		infin = initial()
		c = infin[0]
		conn = infin[1]
		subject = input(colored("Enter subject name : ",'green'))
		link = input(colored("Enter google-meet link : ",'green'))
		c.execute("INSERT INTO subject_list (subject,link) VALUES(?, ?)",(subject, link))
		conn.commit()
		if input("\nDo you want to stop adding subject?(y/n)").lower() == "y":
			break
	
	


#To display subject and its meet links			
def display_subject_list():
	infin = initial()
	c = infin[0]
	conn = infin[1]
	c.execute("SELECT * FROM subject_list")
	rows = c.fetchall()
	print("\n")
	for row in rows:
		print(*row)
	print("\n")

#To display timetable 
def display_timetable(*week):
	infin = initial()
	c = infin[0]
	con = infin[1]
	if len(week) == 0 :
		week = ["Mon","Tue","Wed","Thus","Fri","Sat","Sun"]
	
	for day in week:
		st = "SELECT * FROM "+day
		c.execute(st)
		print("\n")
		rows = c.fetchall()
		print(colored(day+": ","magenta"))
		for row in rows:
			print(*row)

#################################################################################################
def delete_timetable():


def delete_subject():
		