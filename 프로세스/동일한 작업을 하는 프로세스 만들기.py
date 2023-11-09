01 from multiprocessing import Process
02 import os
03 
04 def foo():
05     print('hello, os')
06   
07 if __name__ == '__main__':
08     child1 = Process(target=foo).start()
09     child2 = Process(target=foo).start()
10     child3 = Process(target=foo).start()
