import re

fhandler = open('regex_sum_2093893.txt')

values = list()

for lines in fhandler:
    integers = re.findall('[0-9]+',lines)

    for num in integers:
        
        values.append(int(num))

print("There are",len(values) ,"values with a sum of ",sum(values))



