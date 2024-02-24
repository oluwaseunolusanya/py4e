import json

data = '''
    {
        "name": "Olu",
        "phone":{
            "type": "intl",
            "number":"+44 123 456 7777"
        },
        "email": {
            "hide": "yes"
        }
    }
'''
info = json.loads(data)
print("Name:", info["name"])
print("Email hidden:",info["email"]["hide"])