from json.decoder import JSONDecodeError
import requests


#payload = {"name": "User"}
# создаем GET запрос на указанный адрес и печатаем json-ответ
#response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#print(response.text)


response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")