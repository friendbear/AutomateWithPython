#! python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://login.yahoo.com/')

email_elem = browser.find_element_by_id('login-username')
email_elem.send_keys('not_my_real_email')
email_elem.submit()

#password_elem = browser.get_element_by_id('login-passwd')
#password_elem.send_keys('12345')

#password_elem.submit()
