# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser

class OpsTestcase08rechargereturncrash(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase08_rechargereturncrash(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(7) a").click()
        driver.implicitly_wait(10)
        print driver.title
        driver.find_element_by_css_selector("div#container.container a.btn.btn-sm.btn-info").send_keys(Keys.ENTER)
        
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_id("recharge_setting_form_money_give").clear()
        driver.find_element_by_id("recharge_setting_form_money_give").send_keys("100")
        driver.find_element_by_id("recharge_setting_form_min").clear()
        driver.find_element_by_id("recharge_setting_form_min").send_keys("100")
        driver.find_element_by_id("recharge_setting_form_max").clear()
        driver.find_element_by_id("recharge_setting_form_max").send_keys("1000")
        driver.find_element_by_name("commit").click()
        
        addchizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print addchizhifanxian
        #self.assertEqual(addchizhifanxian, u"返现设置已添加")
        
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("recharge_setting_form_min").clear()
        driver.find_element_by_id("recharge_setting_form_min").send_keys("200")
        driver.find_element_by_name("commit").click()
        #html body div#container.container div.alert.fade.in.alert-success
        editchizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print editchizhifanxian
        #self.assertEqual(editchizhifanxian, u"返现设置已更新")
        
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child.btn.btn-sm.btn-danger
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"删除").click()
        time.sleep(2)
        self.assertEqual(u"确认删除", self.close_alert_and_get_its_text())
        #driver.find_element_by_link_text(u"城市管理").click()
        #html body div#container.container
        deletechizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print deletechizhifanxian
        #self.assertEqual(deletechizhifanxian, u"返现设置删除成功")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
