import requests

# создаем GET запрос на указанный адрес и печатаем json-ответ
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)
