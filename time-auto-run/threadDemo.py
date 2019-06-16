#! python3

import threading, time

print('main thread start')
def take_a_nap():
    time.sleep(5)
    print('awake')

#function = lambda sleep5: time.sleep(5)

thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()


thread_obj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
                                           kwargs={'sep': ' & '})
thread_obj.start()

print('main thread end')
