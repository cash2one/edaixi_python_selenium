
#-*- conding=utf-8 -*-

from selenium import webdriver

#my testcase for python 
browser = webdriver.Firefox()
browser.get("http://www.yahoo.com")

print browser.title
assert "Yahoo!" in browser.title

browser.close()


