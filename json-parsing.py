import urllib.request
import json

url = input('Enter location: ')
print('Retrieving',url)

urlhandler = urllib.request.urlopen(url)
data = urlhandler.read()

print('Retrieved',len(data),'characters')

info = json.loads(data)

comments = info['comments']

count = len(comments)

total_sum = 0
for comment in comments:
    total_sum = total_sum + comment['count']

# Print the results
print('Count:', count)
print('Sum:', total_sum)

