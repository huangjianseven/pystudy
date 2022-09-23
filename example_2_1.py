from threading import Thread
from time import sleep, localtime, strftime

def func(x,y):
    for i in range(x,y):
        print(i,end=' ',flush=True)
    print()
    sleep(10)

t1 = Thread(target=func,args=(15,20))

print('now:', strftime('%Y-%m-%d %H-%M-%S',localtime()))

t1.start()
t1.join(5)

t2 = Thread(target=func,args=(5,10))

print('now:', strftime('%Y-%m-%d %H-%M-%S',localtime()))
t2.start()
t2.join()
print('now:', strftime('%Y-%m-%d %H-%M-%S',localtime()))
