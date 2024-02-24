import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Olu</name>
    <phone type="intl">+44 123 744 2843</phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print("Name:",tree.find("name").text)
print("Attr:",tree.find("email").get("hide"))