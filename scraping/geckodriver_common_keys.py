#! python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://nostarch.com')

# browser
# back, forward, refresh, quit
html_elem = browser.find_element_by_tag_name('html')

# Keys
# DOWN, UP, LEFT, LIGHT
# ENTER, RETURN
# HOME, END, PAGE_DOWN, PAGE_UP
# ESCAPE, BACK_SPACE, DELETE
# F1, F2, ... F12
# TAB
html_elem.send_keys(Keys.END)

time.sleep(2)
html_elem.send_keys(Keys.HOME)

