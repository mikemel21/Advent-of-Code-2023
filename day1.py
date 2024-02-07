'''
Problem:
    Find the sum of all of the calibration values
'''
import re

sum = 0      
with open ("day1Input.txt", "r") as reader:
    for line in reader.readlines():
        # find every number in a line
        cur = re.findall('\d', line)

        # combine first and last number as integer
        num = int(cur[0] + cur[len(cur)-1])
        
        # add to total
        sum += num
print(sum)