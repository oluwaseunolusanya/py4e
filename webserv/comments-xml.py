import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)
# print(uh)

data = uh.read()
# print(type(data))
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)
# print(tree)

counts = tree.findall('.//count')
result = 0
for count in counts:
    result += int(count.text)

print("Count:",len(counts))
print("Sum:",result)
