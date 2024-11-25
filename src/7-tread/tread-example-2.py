import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.name = threadName

    def run(self):
        time.sleep(1)
        print('In run: ', self.name)

    def output(self):
        print('In output: ', self.name)

if __name__ == '__main__':
    t = myThread('test')
    t.start()
    t.output()
    time.sleep(2)
    print('OK')

'''
In output:  test
In run:  test
OK
'''