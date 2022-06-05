import requests

headers = {"some_header": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

# в первом - ответ сервера, какие заголовки он получил в запросе от нашего клиента
# второй - ответ сервера на запрос
print(response.text)
print(response.headers)