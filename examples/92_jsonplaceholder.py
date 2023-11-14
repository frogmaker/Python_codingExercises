"""
JSONplaceholder - miejsce zastępcze na Twoj przyszly json

"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko jest ok")
    print(tasks[0])
