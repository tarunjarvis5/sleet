import Start as s
import Database as db
from termcolor import colored
import os
import sys
os.system('color')

print(colored("\n#####################################################################\n","red"))
print("Sorry for the command line interface we are working on UI")
print(colored("\n#####################################################################\n","red"))
while True:
	print("type in 'help' to display all commands:")
	command = input()
	if command == 'help' :
		print("Type 'timetable'       or '1' to display your timetable ")
		print("Type 'subject'         or '2' to display your subjects and meet link ")
		print("Type 'addsubject'      or '3' to add subjects to your subject-list ")
		print("Type 'addtimetable'    or '4' to add subjects to your time-table ")
		print("Type 'deletetimetable' or '5' to delete anyday's timetable ")
		print("Type 'deletesubject'   or '6' to delete any subject for subject-list ")
		print("Type 'exit' to Exit from SLEET \n")
		command = input()	
	else:
		print("Wrong!!! you literally had to copy the above spelling") 
		
	

	if command == "timetable" or command == "1" :
		db.display_timetable()

	elif command == "subject" or command == "2" :
		db.display_subject_list()

	elif command == "addsubject" or command == "3" :
		db.insertinto_subject_list()

	elif command == "addtimetable" or command == "4" :
		db.insertinto_timetable()

	elif command == "deletetimetable" or command == "5" :
		db.delete_timetable()

	elif command == "deletesubject" or command == "6" :
		db.delete_subject_list()

	elif command == "exit" :
		sys.exit("Bye Bye, That's Rude tho")







print("First enter all your g-meet subject and link in the database")
print("Enter 'yes' if you want to check the subject list in the database: ")
i = input()
if i == "yes" :
	db.print_database()

#b = input("subject")
#c = input("link")
db.initial()
#db.insertinto_subject_list()
#db.display_subject_list()

db.insertinto_timetable()
db.display_timetable()

#hile True :
	#if 0 subject the contin asking for entering subject

