import allure
from reqs.baseRequests import BaseRequests
from constants import Constants


class OrderRequests(BaseRequests):

    @allure.step('Создаем заказ методом POST')
    def post_create_order(self, token, data):
        url = Constants.ORDER_URL
        return self.exec_post_request_with_token(url, data=data, token=token)

    @allure.step('Создаем заказ без токена методом POST')
    def post_create_order_no_token(self, data):
        url = Constants.ORDER_URL
        return self.exec_post_request(url, data=data)

    @allure.step('Получаем список ингредиентов методом GET')
    def get_ingredients_list(self):
        url = Constants.INGREDIENTS_URL
        return self.exec_get_request(url)

    @allure.step('Получаем заказы пользователя методом GET')
    def get_user_orders(self, token):
        url = Constants.ORDER_URL
        return self.exec_get_request_with_token(url, token=token)