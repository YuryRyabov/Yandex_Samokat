import requests
from config import BASE_URL

def create_order(data):
    url = BASE_URL + "orders"
    response = requests.post(url, json=data)
    return response

def get_order_by_track(track):
    url = BASE_URL + f"orders/track?t={track}"
    response = requests.get(url)
    return response