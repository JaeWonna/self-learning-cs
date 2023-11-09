import threading
import os

def foo():
    print('this is foo')

def bar():
    print('this is bar') 

def baz():
    print('this is baz')

if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
