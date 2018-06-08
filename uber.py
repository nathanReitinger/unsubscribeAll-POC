##################################################
#            unsubscribe email POC               #
##################################################

import random
import time
from selenium import webdriver
import barnum

addresses = ["@gmail.com", "@yahoo.com" , "@mail.com" , "@outlook.com" , "@inbox.com"]
breaks = [".", "", "_"]

def start():
    path_to_chromedriver = '/home/marvin/node_modules/chromedriver/lib/chromedriver/chromedriver'
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    # when using fry's (https://www.frys.com/workflow/AcctMaint/fryspromocom/unsubc.jsp?site=cemail061416) an email
    # confirmation is generated along with an HTML indicator that the user existed in the database
    url = 'https://www.uber.com/unsubscribe/'
    browser.get(url)
    return browser

def getALL():
    '''
    using a simple random-realistic name generator
    [reference] https://github.com/chris1610/barnum-proj
    :return: first name, last name, and email address (here we are only using the email address)
    '''
    name = barnum.gen_data.create_name()

    first_name = name[0]
    last_name = name[1]
    email_address = first_name + breaks[random.randint(0, 2)] + last_name + addresses[random.randint(0, 4)]

    return first_name, last_name, email_address

while True:
    '''
    repetitive launch-quit of the chrome browser
    grabs random email address and inserts it into the unsubscribe form (could be done for cell phone too)
    '''
    browser = start()
    first_name, last_name, email_address = getALL()

    email = browser.find_element_by_xpath('//*[@id="email-unsubscribe"]')
    email.send_keys(email_address)

    browser.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div[5]/div/div/div/div[2]/div/div[1]/div/div[2]/a').click()
    time.sleep(10)

    # used in a loop method of form entry (rather than quitting the browser)
    # browser.find_element_by_xpath('//*[@id="email-unsubscribe"]').clear()

    # repetitive launch and quit
    browser.quit()
