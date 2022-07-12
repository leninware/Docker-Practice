import requests

# res = requests.delete("http://127.0.0.1:5001/api/cars/3")
res = requests.post("http://127.0.0.1:5001/api/cars/2", {"model": "Ford", "color": "Yellow", "sold": True})
print(res.json())
