import sqlite3
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
	lst = ["mon","tue","wed","thu","fri","sat"]
	for i in range(0,6):
		st = "CREATE TABLE IF NOT EXISTS "+lst[i]+" (subject TEXT, timestart TEXT, timeend TEXT)"
		c.execute(st)


# To insert Time table	
def insertinto_timetable(day,subject,timest,timend):
	infin = initial()
	c = infin[0]
	conn = infin[1]
	day = day.lower()
	day = day[:3]
	st = "INSERT INTO "+day+" (subject,timestart,timeend) VALUES( ?, ?, ?)"
	c.execute(st,(subject, timest, timend))
	conn.commit()

			
#To insert subject and link for the meeting
def insertinto_subject_list(subject, link):
	infin = initial()
	c = infin[0]
	conn = infin[1]
	c.execute("INSERT INTO subject_list (subject,link) VALUES(?, ?)",(subject, link))
	conn.commit()



#To subject and its meet links
def subject_list():
	infin = initial()
	c = infin[0]
	conn = infin[1]
	c.execute("SELECT * FROM subject_list")
	rows = c.fetchall()
	return rows


#To display timetable 
def timetable(day):
	infin = initial()
	c = infin[0]
	con = infin[1]
	st = "SELECT * FROM "+day
	c.execute(st)
	rows = c.fetchall()
	return rows

#To delete timetable
def delete_timetable(day):
	infin = initial()
	c = infin[0]
	conn = infin[1]
	st = "DROP TABLE IF EXISTS "+day
	c.execute(st)
	conn.commit()
	initialize_table()


# To delete subject list 
def delete_subject():
		infin = initial()
		c = infin[0]
		conn = infin[1]
		st = "DROP TABLE IF EXISTS subject_list"
		c.execute(st)
		conn.commit()
		initialize_table()


def get_day(day):
	infin = initial()
	c = infin[0]
	conn = infin[1]
	st = "SELECT * FROM " + day
	c.execute(st)
	rows = c.fetchall()
	return rows

def get_link(lec):
	infin = initial()
	c = infin[0]
	conn = infin[1]
	st = "SELECT * FROM subject_list"
	c.execute(st)
	rows = c.fetchall()
	for row in rows:
		if row[0] == lec :
			return row[1]
