fname = input("Enter file name:")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhandler = open(fname)

hrcount = dict()

for line in fhandler:
    if not line.startswith('From '):
        continue
    line = line.split() #split line to words
    hrs = line[5]       #time is in the 5th index position
    h =  hrs.split(':')[0]   #get hr to display hr is in 0 index of split time

    # Count the occurrences of each hour
    hrcount[h] = hrcount.get(h,0) + 1

for hour in sorted(hrcount):
    print(hour, hrcount[hour])
