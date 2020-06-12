import gevent
from gevent.queue import Queue
from decorator import decorator
import random

q = Queue()

@decorator
def spawn(func,*args,**kwargs):
    gevent.spawn(func,*args,**kwargs)

@spawn
def consummer():
    while 1:
        tmp = q.get()
        print("Received: %s" % tmp)

@spawn
def producer():
    while 1:
        q.put(random.randint(0,100))
        gevent.sleep(5)

consummer()
producer()
gevent.sleep(1)
producer()

while 1:
    gevent.sleep(1)
    print('.')
