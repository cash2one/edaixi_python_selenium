#-*-coding:utf-8-*- 
#coding=utf-8
from appobjectutils import SingleWebDriver
#class appobjectops:
# class appObjectUtils(self):
#     
class appobjectops:
    loginClickButton = "div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
    clickRechargeReturncrashLink= "div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a"
    
    clickNewButtonRechargeReturncrash="div#container.container div a.btn.btn-info.btn-info"
    addchizhifanxianResult="div#container.container div.alert.fade.in.alert-success"
    
    clickEditButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child"
    editchizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
    clickDeleteButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child"
    deletechizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
    def getWebElementOpsRechargereturncrash(self):
        #SingleWebDriver.getWebDriverInstance().find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a").click()
        return SingleWebDriver.getWebDriverInstance(self).find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a")