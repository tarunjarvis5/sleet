import Database as db
import Main as m
import time
#from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def sleet_engine(subject_name, link, lecture_time, day):

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
	driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]").click()