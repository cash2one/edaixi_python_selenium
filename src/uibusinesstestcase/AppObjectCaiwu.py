# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def getCaiwuNagvifator():
    driver = webdriver.Firefox()
    driver.get("/")
    webdriverObject=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
    
    return webdriverObject.text


