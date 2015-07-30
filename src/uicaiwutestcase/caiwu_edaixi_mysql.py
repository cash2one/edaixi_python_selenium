#-*- coding:utf-8 -*-  
#enc oding:utf-8
#mysqldb      
import time, MySQLdb, sys  ,ConfigParser

conf = ConfigParser.ConfigParser()
   
conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
mysqlhostname = conf.get("databaseconn", "mysqlhostname")
mysqlusername = conf.get("databaseconn", "mysqlusername")
mysqlpassword = conf.get("databaseconn", "mysqlpassword")
mysqldatabase = conf.get("databaseconn", "mysqldatabase")

print mysqlhostname,mysqlusername,mysqlpassword, mysqldatabase
conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
global cursor 
cursor = conn.cursor()
n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL order by id") 
for row in cursor.fetchall():
    for ordersn in row: 
        ordersn     
        #print "the random ordersn  is ",ordersn  
#print ordersn
n = cursor.execute("SELECT cardno FROM ims_icard_card WHERE cardno IS NOT NULL order by id") 
for row in cursor.fetchall():
    for huiyuanid in row: 
        huiyuanid  
        
global ordersnnumber,huiyuannumber
ordersnnumber=str(ordersn)
huiyuannumber=str(huiyuanid)
print ordersnnumber,huiyuannumber


#conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
#global cursor ,ordernumber
#cursor = conn.cursor()
n = cursor.execute("SELECT ordersn ,username,tel,address FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL ORDER BY id") 
for i in xrange(cursor.rowcount):
    ordersn ,username,tel,address = cursor.fetchone()
print ordersn ,username,tel,address
#for row in cursor.fetchone():
#    for ordersn in row: 
#        ordersn 
#ordernumber=ordersn[1]
#print ordernumber

'''
cursor.execute("SELECT id, name FROM `table`")
for i in xrange(cursor.rowcount):
 id, name = cursor.fetchone()
 print id, name

cursor.execute("SELECT id, name FROM `table`")
result = cursor.fetchmany()
while result:
 for id, name in result:
  print id, name
 result = cursor.fetchmany()

cursor.execute("SELECT id, name FROM `table`")
for id, name in cursor.fetchall():
 print id, name
        '''
        
        




