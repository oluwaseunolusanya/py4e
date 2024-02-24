import xml.etree.ElementTree as ET

input = '''
<user_data>
    <users>
        <user x= "2">
            <id>001</id>
            <name>Ade</name>
        </user>
        <user x= "7">
            <id>009</id>
            <name>Olu</name>
        </user>     
    </users>
</user_data>
'''

user_data = ET.fromstring(input)
users = user_data.findall("users/user")
print("User count:", len(users))

for user in users:
    print("Name", user.find("name").text)
    print("Id", user.find("id").text)
    print("Attribute", user.get("x"))
