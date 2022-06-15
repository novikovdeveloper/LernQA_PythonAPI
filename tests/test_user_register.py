from LernQA_PythonAPI.lib.my_requests import MyRequests
from LernQA_PythonAPI.lib.base_case import BaseCase
from LernQA_PythonAPI.lib.assertions import Assertions
import pytest
import random
import string


class TestUserRegister(BaseCase):
    exclude_params = [
        {'password': '', 'username': '123', 'firstName': '123', 'lastName': '123', 'email': 'a@rr.nu'},
        {'password': '123', 'username': '', 'firstName': '123', 'lastName': '123', 'email': 'a@rr.nu'},
        {'password': '123', 'username': '123', 'firstName': '', 'lastName': '123', 'email': 'a@rr.nu'},
        {'password': '123', 'username': '123', 'firstName': '123', 'lastName': '', 'email': 'a@rr.nu'},
        {'password': '123', 'username': '123', 'firstName': '123', 'lastName': '123', 'email': ''}
    ]
    error_message = [
        ("The value of 'password' field is too short"),
        ("The value of 'username' field is too short"),
        ("The value of 'firstName' field is too short"),
        ("The value of 'lastName' field is too short"),
        ("The value of 'email' field is too short")
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"


    # - Создание пользователя с некорректным email - без символа @
    def test_create_user_nocorrect_email(self):
        email='lernqaexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == "Invalid email format"

    # - Создание пользователя без указания одного из полей
    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_field(self, condition):
        response = MyRequests.post("/user/", data=condition)
        Assertions.assert_code_status(response, 400)

    #- Создание пользователя с очень коротким именем в один символ
    def test_create_user_short_name(self):
        response = MyRequests.post("/user/", data=
        {'password': '123', 'username': 't', 'firstName': '123', 'lastName': '123', 'email': 'u@yy.mi'})

        Assertions.assert_code_status(response, 400)
        assert response.text == "The value of 'username' field is too short"

    #-Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_long_name(self):
        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(300))
        response = MyRequests.post("/user/", data=
        {'password': '123',
         'username': username,
         'firstName': '123',
         'lastName': '123',
         'email': 'a@rr.nu'})

        print(response.text)

        Assertions.assert_code_status(response, 400)
        assert response.text == "The value of 'username' field is too long"




