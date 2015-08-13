#1.生成随机数  
import random    #这个是注释，引入模块  
rnd = random.randint(1,500)#生成1-500之间的随机数  
      
#2.读文件  
#       
# f = open("c:\\1.txt","r")  
#              lines = f.readlines()#读取全部内容  
#              for line in lines  
#                      print line  
# #3.写文件  
#             f = open("c:\\1.txt","r+")#可读可写模式  
#             f.write("123")#写入字符串  
#       
# #4.正则表达式，读取tomcat的日志并打印日期  
#       
#          import re  
#          regx = "\d\d\d\d-\d\d-\d+"  
#          f = open("c:\stdout.log","r")  
#          i = 0  
#          for str in f.readlines():  
#             if re.search(regx,str):  
#                  Response.write(str+"<br>")  
#                   if i>10:break#由于是测试，只分析十行  
#                   i=i+1  
#          f.close();  
      
#5.连接数据库  
#       
#     import pgdb  
#       
#     conn = pgdb.connect  
#       
#     (host='localhost',databse='qingfeng',user='qingfeng',password='123')  
#       
#             cur = conn.cursor()   
#       
#             cur.execute("select * from dream")   
#       
#             print cur.rowcount  
#       
# #6.SAX处理xml:  
#       
#           import string  
#           from xml.sax import saxlib, saxexts  
#       
#           class QuotationHandler(saxlib.HandlerBase):  
#               """Crude sax extractor for quotations.dtd document"""  
#       
#               def __init__(self):  
#                       self.in_quote = 0  
#                       self.thisquote = ''  
#       
#               def startDocument(self):  
#                   print '--- Begin Document ---'  
#       
#               def startElement(self, name, attrs):  
#                   if name == 'quotation':  
#                       print 'QUOTATION:'  
#                       self.in_quote = 1  
#                   else:  
#                       self.thisquote = self.thisquote + '{'  
#       
#               def endElement(self, name):  
#                   if name == 'quotation':  
#                       print string.join(string.split(self.thisquote[:230]))+'...',  
#                       print '('+str(len(self.thisquote))+' bytes)\n'  
#                       self.thisquote = ''  
#                       self.in_quote = 0  
#                   else:  
#                       self.thisquote = self.thisquote + '}'  
#       
#               def characters(self, ch, start, length):  
#                   if self.in_quote:  
#                       self.thisquote = self.thisquote + ch[start:start+length]  
#       
#           if __name__ == '__main__':  
#               parser  = saxexts.XMLParserFactory.make_parser()  
#               handler = QuotationHandler()  
#               parser.setDocumentHandler(handler)  
#               parser.parseFile(open("sample.xml"))  
#               parser.close()  
#       
#       
#  #7.python的GUI模块标准的是Tkinter,也有QT和MFC的模块，有兴趣的大家自己搜索下  
#       
#             import Tkinter  
#       
#             root=Tkinter.Tk()  
#       
#             my=Label(root,"Welcome to python's world")  
#       
#             my.pack()  
#       
#             root.mainloop()  

#encoding=utf-8  
# import web  
# import tagparser  
# db = web.database(dbn='mysql',user='root', pw='', db='webpy')  
# count=0  
# for i in range(10000,10):  
#     url='http://www.baidu.com/s?wd=site%3Aamazon.cn%20dp%2FB&pn='+str(i)+'&tn=baiduhome_pg'  
#     p=tagparser.TagParser()  
#     p.fetchUrl(url)  
#     for t in p.tagList:  
#         a=t.find('dp/B0')  
#         if a>0:  
#             t=t[a+3:a+19]  
#             s=t.split('"')  
#             t=s[0]  
#             s=t.split('/')  
#             t=s[0]  
#             db.insert('productid',productID=t,id=count)  
#             count+=1  
# print 'successed' 
# 
# 
#     __author__ = 'yang'  
#     import MySQLdb  
#     class MySQLHelper:  
#         def __init__(self,host,user,password,charset="utf8"):  
#             self.host=host  
#             self.user=user  
#             self.password=password  
#             self.charset=charset  
#             try:  
#                 self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.password)  
#                 self.conn.set_character_set(self.charset)  
#                 self.cur=self.conn.cursor()  
#             except MySQLdb.Error as e:  
#                 print("Mysql Error %d: %s" % (e.args[0], e.args[1]))  
#       
#       
#         def selectDb(self,db):  
#           try:  
#               self.conn.select_db(db)  
#           except MySQLdb.Error as e:  
#               print("Mysql Error %d: %s" % (e.args[0], e.args[1]))  
#       
#         def query(self,sql):  
#             try:  
#                n=self.cur.execute(sql)  
#                return n  
#             except MySQLdb.Error as e:  
#                print("Mysql Error:%s\nSQL:%s" %(e,sql))  
#       
#         def queryRow(self,sql):  
#             self.query(sql)  
#             result = self.cur.fetchone()  
#             return result  
#       
#         def queryAll(self,sql):  
#             self.query(sql)  
#             result=self.cur.fetchall()  
#             desc =self.cur.description  
#             d = []  
#             for inv in result:  
#                  _d = {}  
#                  for i in range(0,len(inv)):  
#                      _d[desc[i][0]] = str(inv[i])  
#                  d.append(_d)  
#             return d  
#       
#         def insert(self,p_table_name,p_data):  
#             for key in p_data:  
#                 p_data[key] = "'""'"+str(p_data[key])+"'"  
#             key   = ','.join(p_data.keys())  
#             value = ','.join(p_data.values())  
#             real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value + ")"  
#             #self.query("set names 'utf8'")  
#             return self.query(real_sql)  
#       
#       
#         def getLastInsertId(self):  
#             return self.cur.lastrowid  
#       
#         def rowcount(self):  
#             return self.cur.rowcount  
#       
#         def commit(self):  
#             self.conn.commit()  
#       
#         def close(self):  
#             self.cur.close()  
#             self.conn.close()  
#             
#             
#             
# #             threading.Thread
# # 
# # 　　Thread是threading模块中最重要的类之一，可以使用它来创建线程。有两种方式来创建线程：一种是通过继承Thread类，重写它的run方法；另一种是创建一个threading.Thread对象，在它的初始化函数（__init__）中将可调用对象作为参数传入。下面分别举例说明。先来看看通过继承threading.Thread类来创建线程的例子：
# # 
# #  
# #  
# # 
# #     #coding=gbk   
# #     import threading, time, random  
# #     count = 0  
# #     class Counter(threading.Thread):  
# #         def __init__(self, lock, threadName):  
# #             ''''''''@summary: 初始化对象。  
# #              
# #             @param lock: 琐对象。  
# #             @param threadName: 线程名称。  
# #             ''''''''  
# #             super(Counter, self).__init__(name = threadName)  #注意：一定要显式的调用父类的初始   
# #     化函数。  
# #             self.lock = lock  
# #           
# #         def run(self):  
# #             ''''''''@summary: 重写父类run方法，在线程启动后执行该方法内的代码。  
# #             ''''''''  
# #             global count  
# #             self.lock.acquire()  
# #             for i in xrange(10000):  
# #                 count = count + 1  
# #             self.lock.release()  
# #     lock = threading.Lock()  
# #     for i in range(5):   
# #         Counter(lock, "thread-" + str(i)).start()  
# #     time.sleep(2)   #确保线程都执行完毕   
# #     print count  
# # 
# #     #coding=gbk  
# #     import threading, time, random  
# #     count = 0  
# #     class Counter(threading.Thread):  
# #     def __init__(self, lock, threadName):  
# #     ''''''''@summary: 初始化对象。  
# #     @param lock: 琐对象。  
# #     @param threadName: 线程名称。  
# #     ''''''''  
# #     super(Counter, self).__init__(name = threadName)  #注意：一定要显式的调用父类的初始  
# #     化函数。  
# #     self.lock = lock  
# #     def run(self):  
# #     ''''''''@summary: 重写父类run方法，在线程启动后执行该方法内的代码。  
# #     ''''''''  
# #     global count  
# #     self.lock.acquire()  
# #     for i in xrange(10000):  
# #     count = count + 1  
# #     self.lock.release()  
# #     lock = threading.Lock()  
# #     for i in range(5):  
# #     Counter(lock, "thread-" + str(i)).start()  
# #     time.sleep(2)   #确保线程都执行完毕  
# #     print count  
# # 
# #  
# # 
# # 　　在代码中，我们创建了一个Counter类，它继承了threading.Thread。初始化函数接收两个参数，一个是琐对象，另一个是线程的名称。在Counter中，重写了从父类继承的run方法，run方法将一个全局变量逐一的增加10000。在接下来的代码中，创建了五个Counter对象，分别调用其start方法。最后打印结果。这里要说明一下run方法和start方法: 它们都是从Thread继承而来的，run()方法将在线程开启后执行，可以把相关的逻辑写到run方法中（通常把run方法称为活动[Activity]。）；start()方法用于启动线程。
# # 
# #  
# # 
# # 　　再看看另外一种创建线程的方法：
# # 
# #  
# #  
# # 
# #     import threading, time, random  
# #     count = 0  
# #     lock = threading.Lock()  
# #     def doAdd():  
# #         ''''''''@summary: 将全局变量count 逐一的增加10000。  
# #         ''''''''  
# #         global count, lock  
# #         lock.acquire()  
# #         for i in xrange(10000):  
# #             count = count + 1  
# #         lock.release()  
# #     for i in range(5):  
# #         threading.Thread(target = doAdd, args = (), name = ''thread-'' + str(i)).start()  
# #     time.sleep(2)   #确保线程都执行完毕   
# #     print count  
# # 
# #     import threading, time, random  
# #     count = 0  
# #     lock = threading.Lock()  
# #     def doAdd():  
# #     ''''''''@summary: 将全局变量count 逐一的增加10000。  
# #     ''''''''  
# #     global count, lock  
# #     lock.acquire()  
# #     for i in xrange(10000):  
# #     count = count + 1  
# #     lock.release()  
# #     for i in range(5):  
# #     threading.Thread(target = doAdd, args = (), name = ''thread-'' +  
# #     str(i)).start()  
# #     time.sleep(2)   #确保线程都执行完毕  
# #     print count  
# # 
# #  
# # 
# # 　　在这段代码中，我们定义了方法doAdd，它将全局变量count逐一的增加10000。然后创建了5个Thread对象，把函数对象doAdd作为参数传给它的初始化函数，再调用Thread对象的start方法，线程启动后将执行doAdd函数。这里有必要介绍一下threading.Thread类的初始化函数原型：
# # def __init__(self, group=None, target=None, name=None, args=(),kwargs={})
# # 　　参数group是预留的，用于将来扩展；
# # 　　参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行；
# # 　　参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
# # 　　参数args和kwargs分别表示调用target时的参数列表和关键字参数。
# # 
# #  
# # 
# # Thread类还定义了以下常用方法与属性：
# # Thread.getName()
# # Thread.setName()
# # Thread.name
# # 
# # 　　用于获取和设置线程的名称。
# # Thread.ident
# # 
# # 　　获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。
# # Thread.is_alive()
# # Thread.isAlive()
# # 
# # 　　判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断这段时间内，线程是激活的。
# # Thread.join([timeout])
# # 
# # 　　调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。下面举个例子说明join()的使用：
# # 
# #  
# #  
# # 
# #     import threading, time  
# #     def doWaiting():  
# #         print ''start waiting:'', time.strftime(''%H:%M:%S'')  
# #         time.sleep(3)  
# #         print ''stop waiting'', time.strftime(''%H:%M:%S'')  
# #     thread1 = threading.Thread(target = doWaiting)  
# #     thread1.start()  
# #     time.sleep(1)  #确保线程thread1已经启动   
# #     print ''start join''  
# #     thread1.join()  #将一直堵塞，直到thread1运行结束。   
# #     print ''end join''  
# # 
# #     import threading, time  
# #     def doWaiting():  
# #     print ''start waiting:'', time.strftime(''%H:%M:%S'')  
# #     time.sleep(3)  
# #     print ''stop waiting'', time.strftime(''%H:%M:%S'')  
# #     thread1 = threading.Thread(target = doWaiting)  
# #     thread1.start()  
# #     time.sleep(1)  #确保线程thread1已经启动  
# #     print ''start join''  
# #     thread1.join()  #将一直堵塞，直到thread1运行结束。  
# #     print ''end join''  
# # 
# #  
# # threading.RLock和threading.Lock
# # 
# # 　　在threading模块中，定义两种类型的琐：threading.Lock和threading.RLock。它们之间有一点细微的区别，通过比较下面两段代码来说明：
# # 
# #  
# #  
# # 
# #     import threading  
# #     lock = threading.Lock() #Lock对象   
# #     lock.acquire()  
# #     lock.acquire()  #产生了死琐。   
# #     lock.release()  
# #     lock.release()  
# # 
# #     import threading  
# #     lock = threading.Lock() #Lock对象  
# #     lock.acquire()  
# #     lock.acquire()  #产生了死琐。  
# #     lock.release()  
# #     lock.release()  
# # 
# #  
# # 
# #  
# #  
# # 
# #     import threading  
# #     rLock = threading.RLock()  #RLock对象   
# #     rLock.acquire()  
# #     rLock.acquire() #在同一线程内，程序不会堵塞。   
# #     rLock.release()  
# #     rLock.release()  
# # 
# #     import threading  
# #     rLock = threading.RLock()  #RLock对象  
# #     rLock.acquire()  
# #     rLock.acquire() #在同一线程内，程序不会堵塞。  
# #     rLock.release()  
# #     rLock.release()  
# # 
# # 
# # 　　这两种琐的主要区别是：RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
# # 
# #  
# # threading.Condition
# # 
# # 　　可以把Condiftion理解为一把高级的琐，它提供了比Lock,RLock更高级的功能，允许我们能够控制复杂的线程同步问题。threadiong.Condition在内部维护一个琐对象（默认是RLock），可以在创建Condigtion对象的时候把琐对象作为参数传入。Condition也提供了acquire,release方法，其含义与琐的acquire,release方法一致，其实它只是简单的调用内部琐对象的对应的方法而已。Condition还提供了如下方法(特别要注意：这些方法只有在占用琐(acquire)之后才能调用，否则将会报RuntimeError异常。)：
# # Condition.wait([timeout]):  
# # 
# # 　　wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。
# # Condition.notify():
# # 
# # 　　唤醒一个挂起的线程（如果存在挂起的线程）。注意：notify()方法不会释放所占用的琐。
# # Condition.notify_all()
# # Condition.notifyAll()
# # 
# # 　　唤醒所有挂起的线程（如果存在挂起的线程）。注意：这些方法不会释放所占用的琐。
# # 
# #  
# # 
# # 　　现在写个捉迷藏的游戏来具体介绍threading.Condition的基本使用。假设这个游戏由两个人来玩，一个藏(Hider)，一个找(Seeker)。游戏的规则如下：1.游戏开始之后，Seeker先把自己眼睛蒙上，蒙上眼睛后，就通知Hider；2.Hider接收通知后开始找地方将自己藏起来，藏好之后，再通知Seeker可以找了； 3.Seeker接收到通知之后，就开始找Hider。Hider和Seeker都是独立的个体，在程序中用两个独立的线程来表示，在游戏过程中，两者之间的行为有一定的时序关系，我们通过Condition来控制这种时序关系。
# # 
# #  
# #  
# # 
# #     #---- Condition   
# #     #---- 捉迷藏的游戏   
# #     import threading, time  
# #     class Hider(threading.Thread):  
# #         def __init__(self, cond, name):  
# #             super(Hider, self).__init__()  
# #             self.cond = cond  
# #             self.name = name  
# #           
# #         def run(self):  
# #             time.sleep(1) #确保先运行Seeker中的方法      
# #               
# #             self.cond.acquire() #b       
# #             print self.name + '': 我已经把眼睛蒙上了''  
# #             self.cond.notify()  
# #             self.cond.wait() #c       
# #                              #f    
# #             print self.name + '': 我找到你了 ~_~''  
# #             self.cond.notify()  
# #             self.cond.release()  
# #                                 #g   
# #             print self.name + '': 我赢了''   #h   
# #               
# #     class Seeker(threading.Thread):  
# #         def __init__(self, cond, name):  
# #             super(Seeker, self).__init__()  
# #             self.cond = cond  
# #             self.name = name  
# #         def run(self):  
# #             self.cond.acquire()  
# #             self.cond.wait()    #a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占   
# #     有琐。  
# #                                 #d   
# #             print self.name + '': 我已经藏好了，你快来找我吧''  
# #             self.cond.notify()  
# #             self.cond.wait()    #e   
# #                                 #h   
# #             self.cond.release()   
# #             print self.name + '': 被你找到了，哎~~~''  
# #               
# #     cond = threading.Condition()  
# #     seeker = Seeker(cond, ''seeker'')  
# #     hider = Hider(cond, ''hider'')  
# #     seeker.start()  
# #     hider.start()  
# # 
# #     #---- Condition  
# #     #---- 捉迷藏的游戏  
# #     import threading, time  
# #     class Hider(threading.Thread):  
# #     def __init__(self, cond, name):  
# #     super(Hider, self).__init__()  
# #     self.cond = cond  
# #     self.name = name  
# #     def run(self):  
# #     time.sleep(1) #确保先运行Seeker中的方法  
# #     self.cond.acquire() #b  
# #     print self.name + '': 我已经把眼睛蒙上了''  
# #     self.cond.notify()  
# #     self.cond.wait() #c  
# #     #f  
# #     print self.name + '': 我找到你了 ~_~''  
# #     self.cond.notify()  
# #     self.cond.release()  
# #     #g  
# #     print self.name + '': 我赢了''   #h  
# #     class Seeker(threading.Thread):  
# #     def __init__(self, cond, name):  
# #     super(Seeker, self).__init__()  
# #     self.cond = cond  
# #     self.name = name  
# #     def run(self):  
# #     self.cond.acquire()  
# #     self.cond.wait()    #a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占  
# #     有琐。  
# #     #d  
# #     print self.name + '': 我已经藏好了，你快来找我吧''  
# #     self.cond.notify()  
# #     self.cond.wait()    #e  
# #     #h  
# #     self.cond.release()  
# #     print self.name + '': 被你找到了，哎~~~''  
# #     cond = threading.Condition()  
# #     seeker = Seeker(cond, ''seeker'')  
# #     hider = Hider(cond, ''hider'')  
# #     seeker.start()  
# #     hider.start()  
# # 
# #  
# # threading.Event
# # 
# # 　　Event实现与Condition类似的功能，不过比Condition简单一点。它通过维护内部的标识符来实现线程间的同步问题。（threading.Event和.NET中的System.Threading.ManualResetEvent类实现同样的功能。）
# # Event.wait([timeout])
# # 
# # 　　堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
# # Event.set()
# # 
# # 　　将标识位设为Ture
# # Event.clear()
# # 
# # 　　将标识伴设为False。
# # Event.isSet()
# # 
# # 　　判断标识位是否为Ture。
# # 
# # 下面使用Event来实现捉迷藏的游戏(可能用Event来实现不是很形象)
# # 
# #  
# #  
# # 
# #     #---- Event   
# #     #---- 捉迷藏的游戏   
# #     import threading, time  
# #     class Hider(threading.Thread):  
# #         def __init__(self, cond, name):  
# #             super(Hider, self).__init__()  
# #             self.cond = cond  
# #             self.name = name  
# #           
# #         def run(self):  
# #             time.sleep(1) #确保先运行Seeker中的方法      
# #               
# #             print self.name + '': 我已经把眼睛蒙上了''  
# #               
# #             self.cond.set()  
# #               
# #             time.sleep(1)     
# #               
# #             self.cond.wait()  
# #             print self.name + '': 我找到你了 ~_~''  
# #               
# #             self.cond.set()  
# #                                   
# #             print self.name + '': 我赢了''  
# #               
# #     class Seeker(threading.Thread):  
# #         def __init__(self, cond, name):  
# #             super(Seeker, self).__init__()  
# #             self.cond = cond  
# #             self.name = name  
# #         def run(self):  
# #             self.cond.wait()  
# #                               
# #             print self.name + '': 我已经藏好了，你快来找我吧''  
# #             self.cond.set()  
# #               
# #             time.sleep(1)  
# #             self.cond.wait()  
# #                                   
# #             print self.name + '': 被你找到了，哎~~~''  
# #               
# #     cond = threading.Event()  
# #     seeker = Seeker(cond, ''seeker'')  
# #     hider = Hider(cond, ''hider'')  
# #     seeker.start()  
# #     hider.start()  
# # 
# #     #---- Event  
# #     #---- 捉迷藏的游戏  
# #     import threading, time  
# #     class Hider(threading.Thread):  
# #     def __init__(self, cond, name):  
# #     super(Hider, self).__init__()  
# #     self.cond = cond  
# #     self.name = name  
# #     def run(self):  
# #     time.sleep(1) #确保先运行Seeker中的方法  
# #     print self.name + '': 我已经把眼睛蒙上了''  
# #     self.cond.set()  
# #     time.sleep(1)  
# #     self.cond.wait()  
# #     print self.name + '': 我找到你了 ~_~''  
# #     self.cond.set()  
# #     print self.name + '': 我赢了''  
# #     class Seeker(threading.Thread):  
# #     def __init__(self, cond, name):  
# #     super(Seeker, self).__init__()  
# #     self.cond = cond  
# #     self.name = name  
# #     def run(self):  
# #     self.cond.wait()  
# #     print self.name + '': 我已经藏好了，你快来找我吧''  
# #     self.cond.set()  
# #     time.sleep(1)  
# #     self.cond.wait()  
# #     print self.name + '': 被你找到了，哎~~~''  
# #     cond = threading.Event()  
# #     seeker = Seeker(cond, ''seeker'')  
# #     hider = Hider(cond, ''hider'')  
# #     seeker.start()  
# #     hider.start()  
# # 
# #  
# # threading.Timer
# # 
# # 　　threading.Timer是threading.Thread的子类，可以在指定时间间隔后执行某个操作。下面是Python手册上提供的一个例子：
# # 
# #  
# #  
# # 
# #     def hello():  
# #         print "hello, world"  
# #     t = Timer(3, hello)  
# #     t.start() # 3秒钟之后执行hello函数。  
# # 
# #     def hello():  
# #     print "hello, world"  
# #     t = Timer(3, hello)  
# #     t.start() # 3秒钟之后执行hello函数。  
# # 
# #  
# # 
# # 　　threading模块中还有一些常用的方法没有介绍：
# # threading.active_count()
# # threading.activeCount()
# # 
# # 　　获取当前活动的(alive)线程的个数。
# # threading.current_thread()
# # threading.currentThread()
# # 
# #  　　获取当前的线程对象（Thread object）。
# # threading.enumerate()
# # 
# #  　　获取当前所有活动线程的列表。
# # threading.settrace(func)
# # 
# # 　　设置一个跟踪函数，用于在run()执行之前被调用。
# # threading.setprofile(func)
# # 
# # 　　设置一个跟踪函数，用于在run()执行完毕之后调用。
# # 
# #  
# # 
# # 　　threading模块的内容很多，一篇文章很难写全，更多关于threading模块的信息，请查询Python手册 threading 模块。
# 
# 
# 
# #!/usr/bin/env python
# # -*- coding: utf-8 -*- 
# u'''对MySQLdb常用函数进行封装的类
#  
#  整理者：兔大侠和他的朋友们（http://www.tudaxia.com）
#  日期：2014-04-22
#  出处：源自互联网，共享于互联网:-)
#  
#  注意：使用这个类的前提是正确安装 MySQL-Python模块。
#  官方网站：http://mysql-python.sourceforge.net/
# '''
# 
# import MySQLdb
# import time
# 
# class MySQL:
#   u'''对MySQLdb常用函数进行封装的类'''
#   
#    error_code = '' #MySQL错误号码
# 
#   _instance = None #本类的实例
#   _conn = None # 数据库conn
#   _cur = None #游标
# 
#   _TIMEOUT = 30 #默认超时30秒
#   _timecount = 0
#     
#   def __init__(self, dbconfig):
#     u'构造器：根据数据库连接参数，创建MySQL连接'
#     try:
#       self._conn = MySQLdb.connect(host=dbconfig['host'],
#                      port=dbconfig['port'], 
#                      user=dbconfig['user'],
#                      passwd=dbconfig['passwd'],
#                      db=dbconfig['db'],
#                      charset=dbconfig['charset'])
#     except MySQLdb.Error, e:
#       self.error_code = e.args[0]
#       error_msg = 'MySQL error! ', e.args[0], e.args[1]
#       print error_msg
#       
#       # 如果没有超过预设超时时间，则再次尝试连接，
#       if self._timecount < self._TIMEOUT:
#         interval = 5
#         self._timecount += interval
#         time.sleep(interval)
#         return self.__init__(dbconfig)
#       else:
#         raise Exception(error_msg)
#     
#     self._cur = self._conn.cursor()
#     self._instance = MySQLdb
# 
#   def query(self,sql):
#     u'执行 SELECT 语句'     
#     try:
#       self._cur.execute("SET NAMES utf8") 
#       result = self._cur.execute(sql)
#     except MySQLdb.Error, e:
#       self.error_code = e.args[0]
#       print "数据库错误代码:",e.args[0],e.args[1]
#       result = False
#     return result
# 
#   def update(self,sql):
#     u'执行 UPDATE 及 DELETE 语句'
#     try:
#       self._cur.execute("SET NAMES utf8") 
#       result = self._cur.execute(sql)
#       self._conn.commit()
#     except MySQLdb.Error, e:
#       self.error_code = e.args[0]
#       print "数据库错误代码:",e.args[0],e.args[1]
#       result = False
#     return result
#     
#   def insert(self,sql):
#     u'执行 INSERT 语句。如主键为自增长int，则返回新生成的ID'
#     try:
#       self._cur.execute("SET NAMES utf8")
#       self._cur.execute(sql)
#       self._conn.commit()
#       return self._conn.insert_id()
#     except MySQLdb.Error, e:
#       self.error_code = e.args[0]
#       return False
#   
#   def fetchAllRows(self):
#     u'返回结果列表'
#     return self._cur.fetchall()
# 
#   def fetchOneRow(self):
#     u'返回一行结果，然后游标指向下一行。到达最后一行以后，返回None'
#     return self._cur.fetchone()
#  
#   def getRowCount(self):
#     u'获取结果行数'
#     return self._cur.rowcount
#               
#   def commit(self):
#     u'数据库commit操作'
#     self._conn.commit()
#             
#   def rollback(self):
#     u'数据库回滚操作'
#     self._conn.rollback()
#        
#   def __del__(self): 
#     u'释放资源（系统GC自动调用）'
#     try:
#       self._cur.close() 
#       self._conn.close() 
#     except:
#       pass
#     
#   def  close(self):
#     u'关闭数据库连接'
#     self.__del__()
#  
# 
# if __name__ == '__main__':
#   '''使用样例'''
#   
#   #数据库连接参数  
#   dbconfig = {'host':'localhost', 
#         'port': 3306, 
#         'user':'dbuser', 
#         'passwd':'dbpassword', 
#         'db':'testdb', 
#         'charset':'utf8'}
#   
#   #连接数据库，创建这个类的实例
#   db = MySQL(dbconfig)
#   
#   #操作数据库
#   sql = "SELECT * FROM `sample_table`"
#   db.query(sql);
#   
#   #获取结果列表
#   result = db.fetchAllRows();
#   
#   #相当于php里面的var_dump
#   print result
#   
#   #对行进行循环
#   for row in result:
#     #使用下标进行取值
#     #print row[0]
#     
#     #对列进行循环
#     for colum in row:
#       print colum
#  
#   #关闭数据库
#   db.close()