# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# Here I want to do some log analysis. the log format can be found below, and we need to calculate the elapse time by the same thread name , and also substract the response and request time.
# Actually, I don't see to much advantage usning panda here. we can do it by pure python and matplotlib.
# 
# 2014/3/23 zhichao li

# <codecell>

from dateutil.parser import parse
from pandas import DataFrame, Series
import pandas as pd
log=[("thread1", "request", "2014-03-22 17:19:42.28"),
     ("thread1", "response", "2014-03-22 17:19:43.28"),
     ("thread1", "request", "2014-03-22 17:19:44.28"),
     ("thread1", "response", "2014-03-22 17:19:45.18"),
     ("thread2", "request", "2014-03-22 17:19:46.28"),
     ("thread2", "response", "2014-03-22 17:19:47.28"),
     ("thread2", "request", "2014-03-22 17:19:48.08"),
     ("thread2", "response", "2014-03-22 17:19:49.28")
     ]
logFrame= pd.DataFrame(
    log,
    columns=['Thread', 'Type', 'Time'])
logFrame['Time'] = logFrame['Time'].map(lambda x: parse(x))
logFrame

# <codecell>

frame1 = logFrame[logFrame['Thread'] == 'thread1']
print type(frame1[0:1])
print type(frame1[0:1]['Time']) #NOTE: Series is per column, not per row.
print frame1[0:1]
print frame1.values

# <headingcell level=2>

# By default plot would transfer the xAix to int.

# <codecell>

frame1 = logFrame[logFrame['Thread'] == 'thread1']
print frame1[0:1]
frame2 = logFrame[logFrame['Thread'] == 'thread2']
thread1=frame1.values
request_time = []
elaps_time = []
for i in range(0, len(thread1),2):
    print thread1[i+1][2]
    request_time.append(thread1[i+1][2])
    elaps_time.append((thread1[i+1][2] - thread1[i][2]).total_seconds())
plot(request_time, elaps_time) # request_time is a list of date time, datetime would be transfer to int here somehow 
xticks(rotation=60)

# <headingcell level=2>

# Transfer datetime to String, then use xTicks to do the mapping 

# <codecell>

frame1 = logFrame[logFrame['Thread'] == 'thread1']
print frame1[0:1]
frame2 = logFrame[logFrame['Thread'] == 'thread2']
thread1=frame1.values
request_time = []
elaps_time = []
for i in range(0, len(thread1),2):
    print thread1[i+1][2]
    request_time.append(str(thread1[i+1][2]))
    elaps_time.append((thread1[i+1][2] - thread1[i][2]).total_seconds())
plot(elaps_time)
xticks(range(len(request_time)),request_time,rotation=60)

# <codecell>

frame1 = logFrame[logFrame['Thread'] == 'thread1']
print frame1[0:1]
frame2 = logFrame[logFrame['Thread'] == 'thread2']
thread1=frame1.values
request_time = []
elaps_time = []
for i in range(0, len(thread1),2):
    print thread1[i+1][2]
    request_time.append(str(thread1[i+1][2]))
    elaps_time.append((thread1[i+1][2] - thread1[i][2]).total_seconds())
plot(elaps_time)
xticks(range(len(request_time)),request_time,rotation=60)

# <headingcell level=2>

# Using Series to plot

# <codecell>

request_time=["2014-03-22 17:19:42.280000"]*100
s = Series(np.random.randn(len(request_time)), index=request_time)
s.plot(rot="45")
xticks(rotation=60) # it can also support xTicks , but we cann't set how many ticks from plot method, so I would love to use matplotlib only.

# <codecell>


