from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found element<{}>'.format(elem.tag_name))
except:
    print('Not Found Element')
