from LernQA_PythonAPI.lib.my_requests import MyRequests
from LernQA_PythonAPI.lib.base_case import BaseCase
from LernQA_PythonAPI.lib.assertions import Assertions
import allure
from LernQA_PythonAPI.lib.allure_description import AllureDescription


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # lOGIN
        login_data = {
            'email': email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")


        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

#- Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_user_not_auth(self):
        response = MyRequests.get("/user/2")
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"/user/2",
            data={"username": new_name}
        )

        assert response2.text == "Auth token not supplied"
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем")
    def test_edit_user_another_user(self):
        AllureDescription.add_step("Авторизация пользователя")
        #Auth
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        AllureDescription.add_step("редактирование пользователя")
        # EDIT
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"/user/29790",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        assert response2.text =="Please, do not edit test users with ID 1, 2, 3, 4 or 5."
        Assertions.assert_code_status(response2, 400)

    #- Попытаемся изменить email пользователя,
    # будучи авторизованными тем же пользователем, на новый email без символа @

    def test_edit_user_uncorrect_email(self):
        #Auth
        data = {
            'email': 'a@rr.nu',
            'password': '123'
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # EDIT
        new_email = "arr.nu"

        response2 = MyRequests.put(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        assert response2.text == "Invalid email format"
        Assertions.assert_code_status(response2, 400)

    #- Попытаемся изменить firstName пользователя,
    # будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    def test_edit_user_change_name_duplicate(self):
        #Auth
        data = {
            'email': 'a@rr.nu',
            'password': '123'
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # EDIT
        new_firstName= "a"

        response2 = MyRequests.put(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_firstName}
        )

        response2_dict = response2.json()
        assert response2_dict.get('error') == 'Too short value for field firstName'
        Assertions.assert_code_status(response2, 400)