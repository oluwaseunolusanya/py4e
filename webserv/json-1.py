import urllib.request, urllib.parse, urllib.error
import json

address = input("Enter location: ")
print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print(info)

# result = 0
# for count in counts:
#     result += int(count.text)

# print("Count:",len(counts))
# print("Sum:",result)