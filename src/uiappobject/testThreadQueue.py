import ThreadedWorker
import Queue
 
urls_to_process = ["http://facebook.com", "http://pypix.com"]
 
work_queue = Queue()
result_queue = Queue()
 
def process_url(url):
    # TODO: Do some work with the url
    return url
 
def main():
    # spawn a pool of threads, and pass them queue instance 
    for i in range(5):
        t = ThreadedWorker(work_queue, result_queue, work_func=process_url)
        t.setDaemon(True)
        t.start()
 
    # populate queue with <span style="width: auto; height: auto; float: none;" id="1_nwp"><a style="text-decoration: none;" mpid="1" target="_blank" href="http://cpro.baidu.com/cpro/ui/uijs.php?adclass=0&app_id=0&c=news&cf=1001&ch=0&di=128&fv=18&is_app=0&jk=f0a05c79bd80b83&k=data&k0=data&kdi0=0&luki=5&n=10&p=baidu&q=06011078_cpr&rb=0&rs=1&seller_id=1&sid=830bd89bc7050a0f&ssp2=1&stid=0&t=tpclicked3_hc&td=1922429&tu=u1922429&u=http%3A%2F%2Fwww%2Eadmin10000%2Ecom%2Fdocument%2F4188%2Ehtml&urlid=0" id="1_nwl"><span style="color:#0000ff;font-size:14px;width:auto;height:auto;float:none;">data</span></a></span>   
    for url in urls_to_process:
        work_queue.put(url)
 
    # wait on the queue until everything has been processed     
    work_queue.join()
 
    # print results
    print(repr(result_queue))
 
main()