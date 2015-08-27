import threadpool
import time
import urllib2
 
urls = [
    'http://www.google.com', 
    'http://www.amazon.com', 
    'http://www.ebay.com', 
    'http://www.alibaba.com', 
    'http://www.reddit.com'
]
 
def myRequest(url):
    resp = urllib2.urlopen(url)
    print url, resp.getcode()
 
 
def timeCost(request, n):
  print "Elapsed time: %s" % (time.time()-start)
 
start = time.time()
pool = threadpool.ThreadPool(5)
reqs = threadpool.makeRequests(myRequest, urls, timeCost)
[ pool.putRequest(req) for req in reqs ]
pool.wait()