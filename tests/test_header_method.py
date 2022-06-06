import requests


class TestMethodHeaders:
    def test_method_header(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_header')
        assert response.headers['x-secret-homework-header'] == "Some secret value", "Secret header was change"