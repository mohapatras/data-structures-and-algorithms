"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from operator import itemgetter
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_time = {}
for call in calls:
    # Dialer phone
    call_time[call[0]] = call_time.get(call[0],0) + int(call[3])
    # Receiver phone
    call_time[call[1]] = call_time.get(call[1],0) + int(call[3])
    # total time
    sum_time = max(call_time.items(), key=itemgetter(1))

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*sum_time))