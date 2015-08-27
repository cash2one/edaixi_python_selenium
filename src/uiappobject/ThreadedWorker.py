import threading
import logging
import Queue
 
def do_threaded_work(work_items, work_func, num_threads=None, per_sync_timeout=1, preserve_result_ordering=True):
    """ Executes work_func on each work_item. Note: Execution order is not preserved, but output ordering is (optionally).
 
        Parameters:
        - num_threads               Default: len(work_items)  --- Number of threads to use process items in work_items.
        - per_sync_timeout          Default: 1                --- Each synchronized operation can optionally timeout.
        - preserve_result_ordering  Default: True             --- Reorders result_item to match original work_items ordering.
 
        Return: 
        --- list of results from applying work_func to each work_item. Order is optionally preserved.
 
        Example:
 
        def process_url(url):
            # TODO: Do some work with the url
            return url
 
        urls_to_process = ["http://url1.com", "http://url2.com", "http://site1.com", "http://site2.com"]
 
        # process urls in parallel
        result_items = do_threaded_work(urls_to_process, process_url)
 
        # print(results)
        print(repr(result_items))
    """
    global wrapped_work_func
    if not num_threads:
        num_threads = len(work_items)
 
    work_queue = Queue.Queue()
    result_queue = Queue.Queue()
 
    index = 0
    for work_item in work_items:
        if preserve_result_ordering:
            work_queue.put((index, work_item))
        else:
            work_queue.put(work_item)
        index += 1
 
    if preserve_result_ordering:
        wrapped_work_func = <span style="width: auto; height: auto; float: none;" id="2_nwp"><a style="text-decoration: none;" mpid="2" target="_blank" href="http://cpro.baidu.com/cpro/ui/uijs.php?adclass=0&app_id=0&c=news&cf=1001&ch=0&di=128&fv=18&is_app=0&jk=f0a05c79bd80b83&k=lambda&k0=lambda&kdi0=0&luki=1&n=10&p=baidu&q=06011078_cpr&rb=0&rs=1&seller_id=1&sid=830bd89bc7050a0f&ssp2=1&stid=0&t=tpclicked3_hc&td=1922429&tu=u1922429&u=http%3A%2F%2Fwww%2Eadmin10000%2Ecom%2Fdocument%2F4188%2Ehtml&urlid=0" id="2_nwl"><span style="color:#0000ff;font-size:14px;width:auto;height:auto;float:none;">lambda</span></a></span> work_item: (work_item[0], work_func(work_item[1]))
 
    start_logging_with_thread_info()
 
    #spawn a pool of threads, and pass them queue instance 
    for _ in range(num_threads):
        if preserve_result_ordering:
            t = ThreadedWorker(work_queue, result_queue, work_func=wrapped_work_func, queue_timeout=per_sync_timeout)
        else:
            t = ThreadedWorker(work_queue, result_queue, work_func=work_func, queue_timeout=per_sync_timeout)
        t.setDaemon(True)
        t.start()
 
    work_queue.join()
    stop_logging_with_thread_info()
 
    logging.info('work_queue joined')
 
    result_items = []
    while not result_queue.empty():
        result = result_queue.get(timeout=per_sync_timeout)
        logging.info('found result[:500]: ' + repr(result)[:500])
        if result:
            result_items.append(result)
 
    if preserve_result_ordering:
        result_items = [work_item for index, work_item in result_items]
 
    return result_items
 
class ThreadedWorker(threading.Thread):
    """ Generic Threaded Worker
        Input to work_func: item from work_queue
 
    Example usage:
 
    import Queue
 
    urls_to_process = ["http://url1.com", "http://url2.com", "http://site1.com", "http://site2.com"]
 
    work_queue = Queue.Queue()
    result_queue = Queue.Queue()
 
    def process_url(url):
        # TODO: Do some work with the url
        return url
 
    def main():
        # spawn a pool of threads, and pass them queue instance 
        for i in range(3):
            t = ThreadedWorker(work_queue, result_queue, work_func=process_url)
            t.setDaemon(True)
            t.start()
 
        # populate queue with <span style="width: auto; height: auto; float: none;" id="3_nwp"><a style="text-decoration: none;" mpid="3" target="_blank" href="http://cpro.baidu.com/cpro/ui/uijs.php?adclass=0&app_id=0&c=news&cf=1001&ch=0&di=128&fv=18&is_app=0&jk=f0a05c79bd80b83&k=data&k0=data&kdi0=0&luki=5&n=10&p=baidu&q=06011078_cpr&rb=0&rs=1&seller_id=1&sid=830bd89bc7050a0f&ssp2=1&stid=0&t=tpclicked3_hc&td=1922429&tu=u1922429&u=http%3A%2F%2Fwww%2Eadmin10000%2Ecom%2Fdocument%2F4188%2Ehtml&urlid=0" id="3_nwl"><span style="color:#0000ff;font-size:14px;width:auto;height:auto;float:none;">data</span></a></span>   
        for url in urls_to_process:
            work_queue.put(url)
 
        # wait on the queue until everything has been processed     
        work_queue.join()
 
        # print results
        print repr(result_queue)
 
    main()
    """
 
    def __init__(self, work_queue, result_queue, work_func, stop_when_work_queue_empty=True, queue_timeout=1):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.work_func = work_func
        self.stop_when_work_queue_empty = stop_when_work_queue_empty
        self.queue_timeout = queue_timeout
 
    def should_continue_running(self):
        if self.stop_when_work_queue_empty:
            return not self.work_queue.empty()
        else:
            return True
 
    def run(self):
        while self.should_continue_running():
            try:
                # grabs item from work_queue
                work_item = self.work_queue.get(timeout=self.queue_timeout)
 
                # works on item
                work_result = self.work_func(work_item)
 
                #place work_result into result_queue
                self.result_queue.put(work_result, timeout=self.queue_timeout)
 
            except Queue.Empty:
                logging.warning('ThreadedWorker Queue was empty or Queue.get() timed out')
 
            except Queue.Full:
                logging.warning('ThreadedWorker Queue was full or Queue.put() timed out')
 
            except:
                logging.exception('Error in ThreadedWorker')
 
            finally:
                #signals to work_queue that item is done
                self.work_queue.task_done()
 
def start_logging_with_thread_info():
    try:
        formatter = logging.Formatter('[thread %(thread)-3s] %(message)s')
        logging.getLogger().handlers[0].setFormatter(formatter)
    except:
        logging.exception('Failed to start logging with thread info')
 
def stop_logging_with_thread_info():
    try:
        formatter = logging.Formatter('%(message)s')
        logging.getLogger().handlers[0].setFormatter(formatter)
    except:
        logging.exception('Failed to stop logging with thread info')