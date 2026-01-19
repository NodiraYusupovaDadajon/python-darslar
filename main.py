"""Uyga vazifa, darsda Foydalanuvchi (Users) ma'lumotlarini Json formatida requests yordamida sitedan oldik,
endi siz Posts dan ma'lumotlarni alohida filega darsdagidek chiqarishingiz va file natijasi va kodini
 1 ta filera platformaga yuklashingiz kerak ! Ma'lumotni olish uchun manba:
https://jsonplaceholder.typicode.com/posts"""


import requests
import json
from pprint import pprint

posts = requests.get("https://jsonplaceholder.typicode.com/posts")
royxat = posts.json()
pprint(posts)

json_data = []

for malumotlar in royxat:
    userid = malumotlar["userId"]
    ct_id = malumotlar["id"]
    title_t = malumotlar["title"]
    body_b = malumotlar["body"]




    json_data.append({
        "Foydalanuvchi": userid,
        "Aydisi":  ct_id,
        "sarlavha": title_t,
        "Asosiy matn": body_b
    })

with open("posts.json", mode="w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("posts.json fayli muvafaqiyatli yaratilindi!")