import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
# Number of times to repeat the process
count =int(input("Enter count: "))
# Position of the link to follow (e.g., position 3 means index 2 in Python)
position = int(input("Enter position: ")) - 1

# Loop to repeat the process 'count' times

for i in range(count):
    # Open the URL and read the HTML content
    html = urllib.request.urlopen(url, context=ctx).read()
    data = BeautifulSoup(html, 'html.parser')

    #anchor tags retrieval
    tags = data('a')

    # Print the current URL
    print("Retrieving:", url)

    # Get the link at the desired position
    url = tags[position].get('href',None)

# Print the final URL after the loop completes
print("Retrieving:", url)
