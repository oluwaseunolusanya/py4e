''' The program uses urllib to read the HTML from a URL, extract the href values from the anchor tags, 
    scans for a tag that is in a particular position relative to the first name in the list, follows 
    that link and repeats the process a number of times and reports the last name found. 
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
count = int(input("Enter count:"))
position = int(input("Enter position:"))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

# Retrieve link at the given position and repeat count times.
names = list()
while count > 0:
    url = tags[position - 1].get("href",None)
    print("Retrieving:", url)
    names.append(tags[position - 1].contents[0])
    # print(names)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count -= 1
print("Last name found is",names[-1])