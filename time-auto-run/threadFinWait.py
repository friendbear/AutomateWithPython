#! python3

import threading, time

func = lambda s: print(s)

threads=[]
for thread in range(1, 100):
    t = threading.Thread(target=func, args=[thread])
    threads.append(t)
    t.start()



for thread in threads:
    thread.join()

print('threads join finished.')
