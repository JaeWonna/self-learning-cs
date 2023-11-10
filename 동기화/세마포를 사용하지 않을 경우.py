from threading import Thread

num = 0

def foo():
    for i in range(1000000):
        global num
        num += 1

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=foo)

    t1.start()
    t2.start()

    print(num)
