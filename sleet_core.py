import Database as db
import time
import datetime
import pyautogui
#from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#subject_name, link, lecture_time, day, email, password


def sleet_engine(day,email,password):

	#----------Enabling Microphone, Camera, Geo, Notification Options using ChromeDriver Options and Preferences-----------#

	# Creating chrome driver options object, options enable us to modify
	# chrome options that are not based on web contents but browser settings/options
	opt = webdriver.ChromeOptions()
	# Maximizing browser window
	opt.add_argument("--start-maximized")
	# Pass the argument 1 to allow and 2 to block, name of each preference are self explanatory
	opt.add_experimental_option("prefs", {
    	"profile.default_content_setting_values.media_stream_mic": 1,
    	"profile.default_content_setting_values.media_stream_camera": 1,
    	"profile.default_content_setting_values.geolocation": 2,
    	"profile.default_content_setting_values.notifications": 2
  	})
	
	#----------------------------------------------------------------------------------------------------------------------#
	PATH = "F:\chromedriver.exe"	
	driver = webdriver.Chrome(options=opt, executable_path=PATH)


	driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]").click()
	time.sleep(5)
	driver.find_element_by_id("identifierId").send_keys(email)
	time.sleep(5)
	driver.find_element_by_xpath("// *[ @ id = 'identifierNext'] / div / button").click()
	time.sleep(8)
	driver.find_element_by_name("password").send_keys(password)
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
	time.sleep(8)

	today = db.get_day(day)

	for lec in today :
		subject = lec[1]
		timelecst = lec[2]
		timelecnd = lec[3]
		timehourstart = timelecst[:2]
		timeminstart = timelecst[-2:]
		timehourend = timelecnd[:2]
		timeminsend = timelecnd[-2:]

		link = db.get_link(subject)
		print(subject)
		print(link)
		print(timelecst)
		print(timelecnd)
		print(timehourstart)
		print(timehourend)
		print(timeminstart)
		print(timeminsend)
		i = 0
		while True:

			if i == 1 :
				break
			if datetime.datetime.now().hour == int(timehourstart) and datetime.datetime.now().minute == int(timeminstart) :
				
				driver.get(link)
				time.sleep(10)
				pyautogui.hotkey('ctrl', 'd')
				time.sleep(5)
				pyautogui.hotkey('ctrl','e')
				time.sleep(5)
				driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]").click()
				time.sleep(20)

				while True:
					total = ((int(timehourend)*60)+int(timeminsend)) - ((int(datetime.datetime.now().hour)*60)+int(datetime.datetime.now().minute))

					if int(total) < 5 :
						if datetime.datetime.now().hour == int(timehourend) and datetime.datetime.now().minute == int(timeminsend) :
							driver.get("https://google.com")
							time.sleep(10)
							i = 1
							break
					time.sleep(10)
			time.sleep(10)


