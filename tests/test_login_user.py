from reqs.userRequests import UserRequests
import allure
import pytest


@allure.feature('Проверка авторизации юзера')
class TestUserLogin:
    @allure.title('Существующий пользователь может залогиниться')
    def test_existing_user_log_in(self, create_user_payload, make_user):
        payload = create_user_payload(email='rand', password='1234', name='rand')
        user = make_user(data=payload)
        logged_user = UserRequests().post_login_user(data=payload, token=user["text"]['accessToken'])
        assert logged_user["text"]['user']['email'] == payload['email']

    @allure.title('Пользователь не может залогиниться с неверным логином или паролем')
    def test_user_with_wrong_info_login_fail(self, create_user_payload, make_user, make_fake_name, make_random_value):
        payload = create_user_payload(email='rand', password='1234', name='rand')
        user = make_user(data=payload)
        new_payload_wrong_name = payload.update({'name': make_fake_name})
        user_wrong_name = UserRequests().post_login_user(data=new_payload_wrong_name, token=user["text"]['accessToken'])
        assert (user_wrong_name["status_code"] == 401 and
                user_wrong_name["text"]['message'] == 'email or password are incorrect')
        new_payload_wrong_password = payload.update({'password': make_random_value})
        user_wrong_password = UserRequests().post_login_user(data=new_payload_wrong_password,
                                                             token=user['text']['accessToken'])
        assert (user_wrong_password["status_code"] == 401 and
                user_wrong_password["text"]['message'] == 'email or password are incorrect')