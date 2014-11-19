__author__ = 'vlim'

import threading
import thread
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        # threading.Thread.__init__(self)
        super(myThread, self).__init__()
        self._stop = threading.Event()
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        live(self.name, self.counter, 5)
        print "Exiting " + self.name
    def stop(self):
        print "trying stop"
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()



flag = 1
def live(threadName, delay, counter):
    cur_th = threading.current_thread()
    print "current thread: %s" % cur_th
    print "Start : %s" % time.ctime()
    sec = 0
    while flag:
        time.sleep(delay)
        print "%s-<%s> " % (sec, threadName)
        sec += 1
    print "End : %s" % time.ctime()


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 5)
thread1.start()
thread2.start()

time.sleep(20)
thread1.stop()
# flag = 0
# print "flag: %s" % flag