from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()#fetch html content
soup = BeautifulSoup(html, "html.parser")

#Retrieve all span tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
   
    count = count + 1
    print('TAG:', tag)
    
    value = int(tag.contents[0])

    total = total + value

    
print ("Count:", count)
print("Sum:",total)

   