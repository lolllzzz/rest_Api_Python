import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 90, "name" : "joe", "views": 80000},
        {"likes": 300, "name" : "jack", "views": 4000},
        {"likes": 489, "name" : "joacl", "views": 2000}
    
]

for i in range(len(data)):
    responce = requests.put(BASE + "video/" + str(i), data[i])
    print(responce.json())

input()
responce = requests.patch(BASE + "video/2",{"views":90})
print(responce.json())