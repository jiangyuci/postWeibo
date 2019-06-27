import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def fpost(USRNAME, PASSWORD, TEXT, IMG_PATH):

	# initial browser driver
	'''
	# If FIREFOX is in using
	# download GECKODRIVER from https://github.com/mozilla/geckodriver/releases/
	# make sure their versions match
	'''
	binary = FirefoxBinary('/usr/bin/firefox')
    driver = webdriver.Firefox(firefox_binary=binary)

    '''
    # If CHROME is in using
    # download CHROMEDRIVER from http://chromedriver.storage.googleapis.com/
    # make sure their versions match
    '''
	#chrome_options = Options()
	#chrome_options.add_argument('--headless') # necessary if run on a non-GUI platform
	#chrome_options.add_argument('--no-sandbox') # necessary if run as root
	#driver = webdriver.Chrome('PATH_TO/chromedriver', chrome_options=chrome_options)


	# login 
	driver.get('https://weibo.com')
	time.sleep(10) # wait for website fully loading
	usrId = driver.find_element_by_id('loginname')
	usrId.send_keys(USRNAME)
	passwd = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
	passwd.send_keys(PASSWORD)
	passwd.send_keys(Keys.ENTER)
	time.sleep(10) # wait for login
	

	# text input
	driver.get('https://weibo.com') # weibo always redirect to weibo.com/interests after login
	time.sleep(10)
	text_driver = driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea')
	text_driver.send_keys(TEXT[1])
	text_driver.send_keys(Keys.ENTER) # you may want to change lines
	tpost_driver.send_keys(TEXT[2])

	# pictures input
	pic_driver = driver.find_element_by_name('pic1')
	pic_driver.send_keys(IMG_PATH[1])
	time.sleep(10) # wait for uploading
	pic_driver.send_keys(IMG_PATH[2]) # upload several pics
	time.sleep(10)

	'''
	# you may also want to upload videos
	'''
	# pictures input
	#vid_driver = driver.find_element_by_name('video') 
	#vid_driver.send_keys(VID_PATH) # NOTICE: the VID_PATH is not currently an argument in function!!! Add it 
	#time.sleep(30) # longer time to upload video



	# send post
	'''
	# universal method
	'''
	send_driver = driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a')
	send_driver.click()

	'''
	# only work on mac 
	'''
	# action = ActionChains(driver)
	# action.key_down(Keys.COMMAND).send_keys(Keys.ENTER).key_up(Keys.COMMAND).perform()
	
	'''
	# may work on linux
	'''
	# action = ActionChains(driver)
	# action.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

	#time.sleep(10) # if checking sent post is desirable. uncomment it
	driver.quit() # close the browser
	return True


