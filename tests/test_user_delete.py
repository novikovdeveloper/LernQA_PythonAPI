from LernQA_PythonAPI.lib.my_requests import MyRequests
from LernQA_PythonAPI.lib.base_case import BaseCase
from LernQA_PythonAPI.lib.assertions import Assertions
import pytest

class TestUserDelete(BaseCase):
    def test_try_delete_user_number2(self):
        # Auth
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert response2.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        Assertions.assert_code_status(response2, 400)

    def test_delete_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        response4 = MyRequests.get(f"/user/{user_id}")
        assert response4.text == "User not found"
        Assertions.assert_code_status(response3, 200)

    def test_try_delete_user_anotherUser(self):
        # Auth
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/29790",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        assert response2.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        Assertions.assert_code_status(response2, 400)
