from termcolor import colored
import sys
import os
os.system('color')

def start_initial():
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

    print(colored("\nSleet is a script which allows a user \nto manage their video conference or meet.",'green'))
    print(colored("This is version 1.0 of Sleet",'green'))
    print(colored("Sleet is a bot and many websites do not allow bots so",'cyan'))
    print(colored("*winks in binary*",'green'))
    print(colored("I have a fix.",'cyan'))
    print("Disclaimer : Creator of this script is not responsible for any misuse and the user is using it at his own risk and is responsible for any misuse done.\nThis application was made just for a fun project\nDo you want to continue (y/n):")
    cont = input()
    if cont != "y" :
        sys.exit("OK! bye bye ")

    print("Ensure to type in correct details otherwise the bot won't run and \nmight fail and do something bad\nhe's a bit dumb or she, I don't know we don't discriminate")
    print(colored("\nDon't worry sleet does not save your details,\nyour credentials will be erased after you close the application\n",'yellow'))

def get_details():
    email = input("Enter your email-ID : ")
    password = input("Enter you password : ")
    return [email,password]
