# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner

from wuliu_testcase01_editpermission import *
from wuliu_testcase01_querypermission  import *

from wuliu_testcase02_factory_delivery import *
from wuliu_testcase02_factory_inoutstockquery import *
from wuliu_testcase02_factory_sign import *

from wuliu_testcase03_site_delivery import *
from wuliu_testcase03_site_inoutstockquery import *
from wuliu_testcase03_site_sign import *

from wuliu_testcase04_pushorder import *

from wuliu_testcase05_takecloth import *

from wuliu_testcase06_pushcloth import *

from wuliu_testcase07_accountbalancequery import *

from wuliu_testcase08_citylist_addredit import *
from wuliu_testcase08_citylist_diaodupaidan_fanxidan_yiconfirm import *
from wuliu_testcase08_citylist_diaodupaidan_fanxidan_yipandan import *
from wuliu_testcase08_citylist_diaoduquery_fanxidan import *

from wuliu_testcase09_factory_orderquery import *

from wuliu_testcase10_site_orderquery import *


if __name__ == '__main__':  
    suite = unittest.TestSuite()  

    #caiwu testcase01 first need chongzhi,then koukuan,finally is tuikuan testcase
    suite.addTest(WuliuTestcase01EditPermission('test_wuliu_testcase01_EditPermission'))
    time.sleep(2)
    suite.addTest(WuliuTestcase01Querypermission('test_wuliu_testcase01_querypermission'))
    time.sleep(2)
    #caiwu testcase02
    suite.addTest(WuliuTestcase02factorydelivery('test_wuliu_testcase02_factory_delivery'))
    time.sleep(2)
    suite.addTest(WuliuTestcase02factoryinoutstockquery('test_wuliu_testcase02_factory_inoutstockquery'))
    time.sleep(2)
    suite.addTest(WuliuTestcase02factorysign('test_wuliu_testcase02factory_sign'))
    time.sleep(2)
    #caiwu testcase03s
    suite.addTest(WuliuTestcase03sitedelivery('test_wuliu_testcase03_site_delivery'))
    time.sleep(2)
    suite.addTest(WuliuTestcase03siteinoutstockquery('test_wuliu_testcase03_site_inoutstockquery'))
    time.sleep(2)
    suite.addTest(WuliuTestcase03sitesign('test_wuliu_testcase03_site_sign'))
    time.sleep(2)
    #caiwu testcase04
    suite.addTest(WuliuTestcase04pushorder('test_wuliu_testcase04_pushorder'))
    time.sleep(2)
    #caiwu testcase05
    suite.addTest(WuliuTestcase05takecloth('test_wuliu_testcase05_takecloth'))
    time.sleep(2)
    #caiwu testcase06
    suite.addTest(WuliuTestcase06pushcloth('test_wuliu_testcase06_pushcloth'))
    time.sleep(2)
    #ops testcase07
    suite.addTest(WuliuTestcase07AccountBalance('test_wuliu_testcase07_accountbalance'))
    time.sleep(2)
    #ops testcase08
    suite.addTest(WuliuTestcase08CitylistAddEdit('test_wuliu_testcase08_citylist_addedit'))
    time.sleep(2)
    suite.addTest(WuliuTestcase08citylistdiaodupaidanfanxidanYiPandan('test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yipandan'))
    time.sleep(2)
    suite.addTest(WuliuTestcase08citylistdiaodupaidanfanxidanYiConfirm('test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yiconfirm'))
    time.sleep(2)
    suite.addTest(WuliuTestcase08citylistdiaoduqueryfanxidan('test_wuliu_testcase08_citylist_diaoduquery_fanxidan'))
    time.sleep(2)
    #ops testcase09
    suite.addTest(WuliuTestcase09FactoryOrderQuery('test_wuliu_testcase09_factory_orderquery'))
    time.sleep(2)
    #ops testcase10
    suite.addTest(WuliuTestcase10SiteOrderquery('test_wuliu_testcase10_site_orderquery'))
    time.sleep(2)
    
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-wuliu_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiwuliu testing result",description="201508 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
'''
def test_caiwu_suite():
    suite= unittest.TestSuite()  

    suite.addTest(CaiwuHuiyuancardquery('test_caiwu_huiyuancardquery'))
    suite.addTest(CaiwuUserquery('test_caiwu_userquery'))
    
    suite.addTest(CaiwuShitika('test_caiwu_shitika'))
    suite.addTest(CaiwuShitikaShengchenka('test_caiwu_shitika_shengchenka')) 
    suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    suite.addTest(CaiwuShitikaModify('test_caiwu_shitika_modify'))
    suite.addTest(CaiwuShitikaChongzhi('test_caiwu_shitika_chongzhi'))
    
    suite.addTest(CaiwuYouhuiquangroup('test_caiwu_youhuiquangroup'))
    suite.addTest(CaiwuYouhuiquanlist('test_caiwu_youhuiquanlist'))
    suite.addTest(CaiwuYouhuiquanlistAdd('test_caiwu_youhuiquanlist_add'))
    suite.addTest(CaiwuYouhuiquanlistExport('test_caiwu_youhuiquanlist_export'))
    suite.addTest(CaiwuYouhuiquanlistModify('test_caiwu_youhuiquanlist_modify'))
    

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"caiwu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uicaiwu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
 '''
    