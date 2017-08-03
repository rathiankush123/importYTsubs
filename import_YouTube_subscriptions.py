import sys
import xml.dom.minidom as mini
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def signIntoYoutube(email,password):
    driver.get('https://www.youtube.com/signin')
    emailField = driver.find_element_by_id('identifierId')
    emailField.send_keys(email)
    emailField.send_keys(Keys.ENTER)
    ''' 
        Driver is paused for a small time because,
        after validating email id in google's login page - 
        the HTML content is loaded after a AJAX call. 
        Wait() helps to locate the password field after the content is loaded.
    '''
    driver.implicitly_wait(2)
    passField = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passField.send_keys(password)
    passField.send_keys(Keys.ENTER)

def subscribeToChannels(path_to_xml):

    # parsing the XML export file to get channels list
    dom = mini.parse(path_to_xml)
    outLines = dom.getElementsByTagName('outline')

    # opens a new window in chrome
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    for outLine in outLines:
        try:
            temp = str(outLine.getAttribute('xmlUrl'))
            if len(temp) > 0:
                channel_id = temp[temp.find('?channel_id=')+12:]
                youtube_channel_url = 'https://www.youtube.com/channel/'+channel_id
                driver.get(youtube_channel_url)
                subscribe_btn = driver.find_element_by_class_name('subscribe-label')
                subscribe_btn.click()
        except:
            # if the user is subscribed to the channel already, just pass
            pass

if __name__ == '__main__':

    # parsing the command line arguments
    argv = sys.argv
    path_to_chromedriver = argv[1]
    path_to_YT_channel_xml_file = argv[2]
    email = argv[3]
    password = argv[4]
    driver = webdriver.Chrome(path_to_chromedriver)

    # signing into youtube account
    signIntoYoutube(email, password)

    # opening channel page and clicking subscribe button
    subscribeToChannels(path_to_YT_channel_xml_file)