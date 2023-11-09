01 from multiprocessing import Process
02 import os
03 
04 def foo():
05     print('child process', os.getpid())
06     print('my parent is', os.getppid())
07   
08 if __name__ == '__main__':
09     print('parent process', os.getpid())
10     child = Process(target=foo).start()
