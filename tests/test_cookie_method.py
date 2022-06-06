import requests


class TestCookieMethod:
    def test_cookie_method(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        response_cookie = "<RequestsCookieJar[Cookie(version=0, name='HomeWork', value='hw_value'," \
                          " port=None, port_specified=False, domain='.playground.learnqa.ru', domain_specified=True, " \
                          "domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1650223914, discard=False, " \
                          "comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>"
        assert response_cookie == response.cookies