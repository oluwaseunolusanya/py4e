import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

address = input("Enter location: ")


url = serviceurl + urllib.parse.urlencode({"q":address})

print("Retrieving", url)
html = urllib.request.urlopen(url)
data = html.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None
    
if not js:
    print("==== Failure To Retrieve ====")
# print(js)
print("Plus code", js["features"][0]["properties"]["plus_code"])