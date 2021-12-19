import schedule
from secrets import my_number, mykey
import requests
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': my_number,
        'message': 'Good morning! It is Sunday. This is your reminder to start your week off right. This week you create something great.',
        'key': mykey,
    })
    print(resp.json())

schedule.every().sunday.at('10:00').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
