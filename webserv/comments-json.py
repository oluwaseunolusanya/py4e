import urllib.request, urllib.parse, urllib.error
import json

address = input("Enter location: ")
print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
# print(info)
counts = list()
comments = info["comments"]
# print("Comments has ",len(comments), "elements")
for i in range(len(comments)):
    counts.append(comments[i]["count"])
# print(counts)
print("Count:",len(counts))
print("Sum:",sum(counts))