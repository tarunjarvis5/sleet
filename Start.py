from termcolor import colored
import sys
from getpass import getpass

print(colored('Hello, This is ', 'magenta'))
print(colored('''    
    ssssssss ll            eeeeeeee  eeeeeeee tttttttttttt 
   ss         ll          ee          ee	   tt           
  ss           ll        ee            ee	   tt
    ss         ll        eeeeeeee      eeeeee      tt
      ss       ll        eeeeeeee      eeeeee      tt
	ss     ll        ee            ee          tt     
          ss  ll          ee          ee           tt     
  ssssssss   lllllllllll   eeeeeeee  eeeeeeee      tt       ''','blue'))
print(colored("\nby Tarun Nair",'red'))

print(colored("\nSleet is a web automation bot based script which allows a user \nto manage their video conference or meet.",'green'))
print(colored("This is version 1.0 of Sleet",'green'))
print(colored("Sleet is a bot and many websites do not allow bots so",'cyan'))
print(colored("*winks in binary*",'green'))
print(colored("I have a fix.",'cyan'))
print("Disclaimer : Creator of this script is not responsible for any misuse and the user is using it at his own risk.\nThis application was made just for a fun project\nDo you want to continue (y/n):")
cont = input()
if cont != "y" :
    sys.exit("Wrong! bye bye ")


print("Oh, still here ? atleast take me on a date first")
print("alright alright, eh you're no fun\n")
print("Ensure to type in correct details otherwise the bot won't run and \nmight fail and do something bad\nhe's a bit dumb or she, I don't know we don't discriminate")
email = input("Enter your email-ID : ")
print("Enter your password : ")

print("Don't worry sleet does not save your details,\nyour credentials will be erased after you close the application")
