import requests

url = "https://dummyjson.com/carts"
responce = requests.get(url)
data = responce.json()

print(data["carts"])

for i in data["carts"]:
    for j in i["products"]:
        print(j["price"])
        print("----------------------------")
    print("========================")