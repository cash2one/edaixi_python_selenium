# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner

from kefu_testcase01_feedback_alllist_all import *
from kefu_testcase01_feedback_alllist_answered  import *
from kefu_testcase01_feedback_alllist_filtered import *
from kefu_testcase01_feedback_alllist_needfeedback  import *
from kefu_testcase01_feedback_alllist_noback import *

from kefu_testcase02_myuserfeedback_alllist_all import *
from kefu_testcase02_myuserfeedback_alllist_answered import *
from kefu_testcase02_myuserfeedback_alllist_filtered import *
from kefu_testcase02_myuserfeedback_alllist_needfeedback import *
from kefu_testcase02_myuserfeedback_alllist_noback import *

from kefu_testcase03_orderlist_cancellorder import *
from kefu_testcase03_orderlist_createfanxiorder import *
from kefu_testcase03_orderlist_createorder import *
from kefu_testcase03_orderlist_searchorder import *

from kefu_testcase04_tabmanage_createmastertab import *
from kefu_testcase04_tabmanage_createsubtab import *

from kefu_testcase05_usuallyreply_crud import *
from kefu_testcase05_usuallyreply_search import *

from kefu_testcase06_usuallyquery_chongzhimaquery import *
from kefu_testcase06_usuallyquery_dianzikaquery import *
from kefu_testcase06_usuallyquery_kuaidiyuanquery import *
from kefu_testcase06_usuallyquery_sendsms import *
from kefu_testcase06_usuallyquery_shitikaquery import *
from kefu_testcase06_usuallyquery_telephoneverify import *
from kefu_testcase06_usuallyquery_userquery import *
from kefu_testcase06_usuallyquery_yiwuquery import *
from kefu_testcase06_usuallyquery_youhuiquanquery import *

from kefu_testcase07_estimatemanage_bandinfos import *
from kefu_testcase07_estimatemanage_goodinfos import *
from kefu_testcase07_estimatemanage_middleinfos  import  *



if __name__ == '__main__':  
    suite = unittest.TestSuite()  
 
    #caiwu testcase01 first need chongzhi,then koukuan,finally is tuikuan testcase
    suite.addTest(KefuTestcase01FeedbackAlllistAll('test_kefu_testcase01_feedback_alllist_all'))
    suite.addTest(KefuTestcase01FeedbackAlllistAnswered('test_kefu_testcase01_feedback_alllist_answered'))
    suite.addTest(KefuTestcase01FeedbackAlllistFiltered('test_kefu_testcase01_feedback_alllist_filtered')) 
    suite.addTest(KefuTestcase01FeedbackAlllistNeedFeedback('test_kefu_testcase01_feedback_alllist_needfeedback')) 
    suite.addTest(KefuTestcase01FeedbackAlllistNoback('test_kefu_testcase01_feedback_alllist_noback')) 
    
    #caiwu testcase02
    suite.addTest(KefuTestcase02MyUserFeedbackAlllistAll('test_kefu_testcase02_myuserfeedback_alllist_all'))
    suite.addTest(KefuTestcase02MyUserFeedbackAlllistAnswered('test_kefu_testcase02_myuserfeedback_alllist_answered'))
    suite.addTest(KefuTestcase02MyUserFeedbackAlllistFiltered('test_kefu_testcase02_myuserfeedback_alllist_filtered'))
    suite.addTest(KefuTestcase02MyUserFeedbackAlllistNeedfeedback('test_kefu_testcase02_myuserfeedback_alllist_needfeedback'))
    suite.addTest(KefuTestcase02MyUserFeedbackAlllistNoback('test_kefu_testcase02_myuserfeedback_alllist_noback'))
    
    #caiwu testcase03s
    suite.addTest(KefuTestcase03OrderlistCreateorder('test_kefu_testcase03_orderlist_createorder'))
    suite.addTest(KefuTestcase03OrderlistCreatefanxiorder('test_kefu_testcase03_orderlist_createfanxiorder'))
    suite.addTest(KefuTestcase03OrderlistSearchorder('test_kefu_testcase03_orderlist_searchorder'))
    suite.addTest(KefuTestcase03OrderlistCancellorder('test_kefu_testcase03_orderlist_cancellorder'))
    
    #caiwu testcase04
    suite.addTest(KefuTestcase04TabmanageCreateMastertab('test_kefu_testcase04_tabmanage_createmastertab'))
    suite.addTest(KefuTestcase04TabmanageCreatesubtab('test_kefu_testcase04_tabmanage_createsubtab'))

    #caiwu testcase05
    suite.addTest(KefuTestcase05UsuallyreplySearch('test_kefu_testcase05_usuallyreply_search'))
    suite.addTest(KefuTestcase05UsuallyreplyCrud('test_kefu_testcase05_usuallyreply_crud'))

    #caiwu testcase06
    suite.addTest(KefuTestcase06UsuallyqueryChongzhimaquery('test_kefu_testcase06_usuallyquery_chongzhimaquery'))
    suite.addTest(KefuTestcase06UsuallyqueryDianzikaquery('test_kefu_testcase06_usuallyquery_dianzikaquery'))
    suite.addTest(KefuTestcase06UsuallyqueryKuaidiyuanquery('test_kefu_testcase06_usuallyquery_kuaidiyuanquery'))
    suite.addTest(KefuTestcase06UsuallyquerySendSms('test_kefu_testcase06_usuallyquery_sendsms'))
    suite.addTest(KefuTestcase06UsuallyqueryShitikaquery('test_kefu_testcase06_usuallyquery_shitikaquery'))
    suite.addTest(KefuTestcase06UsuallyqueryTelephoneVerify('test_kefu_testcase06_usuallyquery_telephoneverify'))
    suite.addTest(KefuTestcase06UsuallyqueryUserquery('test_kefu_testcase06_usuallyquery_userquery'))
    suite.addTest(KefuTestcase06UsuallyqueryYiwuquery('test_kefu_testcase06_usuallyquery_yiwuquery'))
    suite.addTest(KefuTestcase06UsuallyqueryYouhuiquanquery('test_kefu_testcase06_usuallyquery_youhuiquanquery'))
    
    #ops testcase07
    suite.addTest(KefuTestcase07EstimatemanageGoodinfos('test_kefu_testcase07_estimatemanage_goodinfos'))
    suite.addTest(KefuTestcase07EstimatemanageMiddleinfos('test_kefu_testcase07_estimatemanage_middleinfos'))
    suite.addTest(KefuTestcase07EstimatemanageBandinfos('test_kefu_testcase07_estimatemanage_bandinfos'))
    


    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-kefu_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uikefu testing result",description="201508 luke")
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
    