# -*- coding: Utf-8 -*-  
import urllib2,urllib,sys,io  
""" 
使用GET在百度搜索引擎上查询 
此例演示如何生成GET串,并进行请求. 
"""  
url = "http://www.baidu.com/s"  
search = [('w','codemo')]  
getString = url + "?" + urllib.urlencode(search)  
  
req = urllib2.Request(getString)  
fd = urllib2.urlopen(req)  
baiduResponse=""  
while 1:  
    data= fd.read(1024)  
    if not len(data):  
        break  
    baiduResponse+=data  
fobj=open("baidu.html",'w')  
fobj.write(baiduResponse)  
fobj.close() 


import sys, urllib2,gzip,StringIO  
  
params = "charset=utf-8&codestring=&token=96f08093303c5c0b3f4a62acb8c04898&isPhone=false&index=0&u=http%3A%2F%2Fwww.baidu.com%2F&safeflg=0&staticpage=https%3A%2F%2Fpassport.baidu.com%2Fv2Jump.html&loginType=1&tpl=mn&callback=parent.bdPass.api.login._postCallback&username=codemo&password=codemopass&verifycode=&mem_pass=on"    
headers = {    
  "Accept": "image/gif, */*",    
  "Referer": "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F",    
  "Accept-Language": "zh-cn",    
  "Content-Type": "application/x-www-form-urlencoded",    
  "Accept-Encoding": "gzip, deflate",    
  "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",    
  "Host": "passport.baidu.com",    
  "Connection": "Keep-Alive",    
  "Cache-Control": "no-cache"    
}  
request = urllib2.Request(  
url = 'https://passport.baidu.com/v2/api/?login',  
data = params,  
headers=headers  
)  
response = urllib2.urlopen(request)  
if response.info().get('Content-Encoding') == 'gzip':  
    print 'gzip enabled'  
    buf = StringIO.StringIO(response.read())  
    f = gzip.GzipFile(fileobj=buf)  
    data = f.read()  
else:  
    data = response.read()  
print "Success-----------------", "\n",data  