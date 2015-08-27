from math import hypot
import time
import urllib2
 
urls = ['http://www.baidu.com', 'http://www.example.com', 'http://www.python.org']
 
def test(url):
    return urllib2.urlopen(url).read()
 
def testIO(nbFutures):
    ts = time.time()
    map(test, urls * nbFutures)
 
    span = time.time() - ts
    print "time spend ", span
 
testIO(1000000)