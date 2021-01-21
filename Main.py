import Start as s
import Database as db
from termcolor import colored
import os
import sys
os.system('color')

print(colored("\n#####################################################################\n","red"))
print("Sorry for the command line interface we are working on UI")
print("type in 'help' to display all commands:")
print(colored("\n#####################################################################\n","red"))

#To create all tables for database
db.initialize_table()

while True:
	print("Enter a command: ")
	command = input()
	if command == 'help' :
		print(colored("Type 'timetable'       or '1' to display your timetable ",'magenta'))
		print(colored("Type 'subject'         or '2' to display your subjects and meet link ",'magenta'))
		print(colored("Type 'addsubject'      or '3' to add subjects to your subject-list ",'magenta'))
		print(colored("Type 'addtimetable'    or '4' to add subjects to your time-table ",'magenta'))
		print(colored("Type 'deletetimetable' or '5' to delete anyday's timetable ",'magenta'))
		print(colored("Type 'deletesubject'   or '6' to delete any subject for subject-list ",'magenta'))
		print(colored("Type 'exit' 		     to Exit from SLEET \n",'magenta'))
		#command = input()	 
		

	elif command == "timetable" or command == "1" :
		db.display_timetable()

	elif command == "subject" or command == "2" or command == "subjects":
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
	
	else:
		print("Wrong!!! you literally had to copy the above spelling")





