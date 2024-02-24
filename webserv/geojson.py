import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({"q":address})

    print("Retrieving", url)
    html = urllib.request.urlopen(url)
    data = html.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat",lat, "lng",lng)
    location = js["results"][0]["formatted_address"]
    print(location)