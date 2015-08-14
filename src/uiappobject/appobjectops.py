#-*-coding:utf-8-*- 
#coding=utf-8
from appobjectutils import SingleWebDriver
#class appobjectops:
# class appObjectUtils(self):
#     
def getWebElementOpsRechargereturncrash(self):
        #SingleWebDriver.getWebDriverInstance().find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a").click()
        return SingleWebDriver.getWebDriverInstance(self).find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a")