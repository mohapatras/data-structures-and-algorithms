"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A
calls_blr = [i for i in calls if i[0].startswith("(080)")]
receiver_num = [i[1] for i in calls_blr]
areas = []

for call in receiver_num:
  if re.search("\(\w+\)", call):
    areas.append(re.search(r'(\(.*?\))', call).group(1))
  elif re.search(r'(^[7|8|9])', call):
    areas.append(call[0:4])
  lexicographic_order = sorted(list(set(areas)))


print(f"The numbers called by people in Bangalore have codes: {lexicographic_order}")

# Part B
total_calls_blr = len(calls_blr)
std_codes_call = len([i for i in calls_blr if i[1].startswith("(080)")])

#percent of calls
percent_calls = round(std_codes_call/total_calls_blr, 4) * 100

print(f"{percent_calls} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

