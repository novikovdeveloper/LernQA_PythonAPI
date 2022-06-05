import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
i = 0
for i in range(len(response.history)):
    print(response.history[i].url)
    i = i + 1
    print(i)
