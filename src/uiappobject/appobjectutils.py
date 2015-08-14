
# -*- coding: utf-8 -*-
#-*- encoding=utf-8 -*-  
from selenium import webdriver

class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  

class SingleWebDriver(Singleton):
    def getWebDriverInstance(self):
        return webdriver.Firefox()
        #return self