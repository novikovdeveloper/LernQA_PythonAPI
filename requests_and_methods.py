import requests

response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response_get.text)
response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "DELETE"})
print(response_delete.text)
response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print(response_post.text)
response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "PUT"})
print(response_put.text)


#1 .С пустым параметром будет выведена ошибка о том что он не предоставлен

response_get_empty = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_get_empty.text)
print(response_get_empty.status_code)

#2.http запрос не из списка. Вернется пустая строка и код 400

response_not_in_list = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"HEAD"})
print(response_not_in_list .text)
print(response_not_in_list .status_code)

#3. Выведется ответ успех с правильным значением

response_right = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print(response_right.text)
print(response_right.status_code)


#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’

parameters_of_methods = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for i in parameters_of_methods:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(f"Метод GET c параметром = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"Метод GET c data = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"Метод POST c data = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(f"Метод POST c параметром = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"Метод PUT c data = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(f"Метод PUT c параметром = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"Метод DELETE c data = {i} имеет статус код {response.status_code} и ответ {response.text}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(f"Метод DELETE c параметром = {i} имеет статус код {response.status_code} и ответ {response.text}")