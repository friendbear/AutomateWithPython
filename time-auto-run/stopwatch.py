#! python3
# stopwatch.py

import time
print('Press Enter Starting. Show duration Press Enter. Finish Ctrl-C')

input()
print('start...')
start_time = time.time()

last_time = start_time

lap_num = 1

# lap time
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)

        print('lap #{}: {} ({})'.format(lap_num, total_time, lap_time), end='')
        lap_num = lap_num + 1
        last_time = now
except KeyboardInterrupt:
    print('Fin.')
