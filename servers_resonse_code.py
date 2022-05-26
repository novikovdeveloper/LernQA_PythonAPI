import requests

#пример редиректа на страницу при параметре allow_redirects=True, false- не идем, и покажутся только данные первого запроса
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)
