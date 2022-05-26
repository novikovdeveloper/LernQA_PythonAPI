import requests

# в pst запросе данные передаются через параметр data, а в get - params 
response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)