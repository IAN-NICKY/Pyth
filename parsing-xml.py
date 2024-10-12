import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")

print('Retrieving', url)
urlhandler = urllib.request.urlopen(url)
data = urlhandler.read()

print('Retrieved', len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for items in counts:
    nums.append(int(items.text))

print('Count:',len(nums))
print('Sum:',sum(nums))

