import requests
import schedule
import time

mobile_number = 085700000000

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey, Good Morning',
        'key': 'textbelt'
    })
    print(resp.json())