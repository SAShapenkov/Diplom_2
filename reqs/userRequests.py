import allure
from reqs.baseRequests import BaseRequests
from constants import Constants


class UserRequests(BaseRequests):
    @allure.step('Создаем пользователя методом POST')
    def post_create_user(self, data=None):
        url = Constants.REGISTER_URL
        return self.exec_post_request(url=url, data=data)

    @allure.step('Логин пользователя методом POST')
    def post_login_user(self, token, data=None):
        url = Constants.USER_LOGIN_URL
        return self.exec_post_request_with_token(url, data=data, token=token)

    @allure.step('Удаляем пользователя методом DELETE')
    def delete_user(self, token):
        url = Constants.USER_EDIT_URL
        return self.exec_delete_request(url, token=token)

    @allure.step('Обновляем данные пользователя методом PATCH')
    def patch_user(self, data, token):
        url = Constants.USER_EDIT_URL
        return self.exec_patch_request(url, data=data, token=token)

    @allure.step('Получаем данные пользователя методом GET')
    def get_user_data(self, token):
        url = Constants.USER_EDIT_URL
        return self.exec_get_request_with_token(url, token=token)