"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

sms_numbers = []
dialers = []
receivers = []
telemarketers = []

for i in texts:
    sms_numbers.append(i[0])
    sms_numbers.append(i[1])
for j in calls:
    dialers.append(j[0])
    dialers.append(j[1])

for ph_no in dialers:
    if ph_no not in receivers:
        if ph_no not in sms_numbers:
            telemarketers.append(ph_no)
final_list = sorted(set(telemarketers))

print("These numbers could be telemarketers: ")
for k in final_list:
    print(k)