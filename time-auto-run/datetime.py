#! python3

import datetime, time

# epoc timestamp
print(datetime.datetime.now())

dt = datetime.datetime(2019, 6, 12, 0, 0, 0)
(y, m, d) = (dt.year, dt.month, dt.day)
print('{}-{}-{}'.format(y, m, d))


datetime.datetime.fromtimestamp(time.time())


# timedelta

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
second = delta.total_seconds()

dt = datetime.datetime.now()
print(dt + datetime.timedelta(days=1000))


oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime("%B of '%y'"))

# change str to datetime
datetime.datetime.strptrime('October 21 2015', '%B %d %Y')
