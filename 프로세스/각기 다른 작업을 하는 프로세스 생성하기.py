01 from multiprocessing import Process
02 import os
03 
04 def foo():
05     print('This is foo')
06
07 def bar():
08     print('This is bar')
09
10 def baz():
11     print('This is baz')
12   
13 if __name__ == '__main__':
14     child1 = Process(target=foo).start()
15     child2 = Process(target=bar).start()
16     child3 = Process(target=baz).start()
