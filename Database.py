import sqlite3
import os

#have to work #############################################################
def initial():
	#check database file
	if os.path.isfile('subject_list.db'):
		pass
	else:
		conn = sqlite3.connect('subject_list.db')

	conn = sqlite3.connect('subject_list.db')
	c = conn.cursor()

	#create subject_list table in database
	c.execute("CREATE TABLE IF NOT EXISTS subject_list (subject TEXT, link TEXT)")

	#create timetable table in database
	#c.execute("CREATE TABLE IF NOT EXISTS timetable (lectureNo INT, Mon TEXT, Tue TEXT, Wed TEXT, Thus TEXT ,Fri TEXT, Sat TEXT)")
	
	return [c,conn]


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
			lectureno = input("input lectureno: ")
			subject = input("input subject: ")
			time = input("input time in 'HH:MM' 24hours format: ")
			st = "INSERT INTO "+lst[i]+" (lectureNo,subject,time) VALUES(?, ?, ?)"
			c.execute(st,(lectureno, subject, time))
			conn.commit()
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

def delete_timetable():
	
	
def delete_subject():
	


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

def display_timetable():
	infin = initial()
	c = infin[0]
	con = infin[1]
	st = "SELECT * FROM Mon"
	c.execute(st)
	rows = c.fetchall()
	print(rows)