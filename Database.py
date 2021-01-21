import sqlite3
import os
from termcolor import colored
import os
os.system('color')

# To initialize database and tables in it
def initial():
	#check database file
	if os.path.isfile('subject_list.db'):
		pass
	else:
		conn = sqlite3.connect('user_database.db')

	conn = sqlite3.connect('user_database.db')
	c = conn.cursor()

	#create subject_list table in database
	c.execute("CREATE TABLE IF NOT EXISTS subject_list (subject TEXT, link TEXT)")

	#create timetable table in database
	i = 0
	lst = ["Mon","Tue","Wed","Thus","Fri","Sat","Sun"]
	for i in range(0,7):	
		st = "CREATE TABLE IF NOT EXISTS "+lst[i]+" (lectureNo INT,subject TEXT, time TEXT)"
		c.execute(st)

	return [c,conn]

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
			
		
# have to work #####################################################################
def insertinto_subject_list():
	while True :
		#conn = sqlite3.connect('subject_list.db')
		#c = conn.cursor()
		infin = initial()
		c = infin[0]
		conn = infin[1]
		b,b1 = input().split()
		c.execute("INSERT INTO subject_list (subject,link) VALUES(?, ?)",(b, b1))
		conn.commit()
		if input("Do you want to stop adding subject?(enter n)").lower() == "n":
			break
	
	


# HAVE TO WORK#######################################################################			
def display_subject_list():
	#conn = sqlite3.connect('subject_list.db')
	#c = conn.cursor()
	infin = initial()
	c = infin[0]
	conn = infin[1]
	c.execute("SELECT * FROM subject_list")
	rows = c.fetchall()
	print(rows)
	for row in rows:
		print(row)

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
		