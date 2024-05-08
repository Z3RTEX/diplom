import requests
import data
import config


def create_order():
    return requests.post(config.BASE_URL + config.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def track_order(track):
    return requests.get(config.BASE_URL + config.RECEIVE_ORDER + str(track))
