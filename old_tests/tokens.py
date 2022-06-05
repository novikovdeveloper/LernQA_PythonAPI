import requests
import time
import json

#1) создать задачу
#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
#3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={})
token = json.loads(create_task.text)["token"]
action_time = json.loads(create_task.text)["seconds"]
response_status_not_ready = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
status_response_not_ready = json.loads(response_status_not_ready.text)["status"]
if status_response_not_ready == "Job is NOT ready":
    print(f"Получен верный статус до того, как задача готова. Статус: '{status_response_not_ready}'")
else:
    print("Получен неверный статус до того, как задача готова")
print(f"{action_time} сек. до конца обратобки запроса")
time.sleep(action_time)
response_status_ready = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
status_response_done = json.loads(response_status_ready.text)["status"]
status_response_result = json.loads(response_status_ready.text)["result"]
if status_response_done == "Job is ready" and status_response_result != '':
    print(f"Получен верный статус и есть поле 'result' ПОСЛЕ того, как задача готова. Статус: '{status_response_done}'")
else:
    print("Получен некорректный статус или отсутствует поле result ПОСЛЕ того, как задача готова")





