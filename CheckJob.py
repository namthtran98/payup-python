import requests
import json


def CheckJob(cookie, us):
    headers = {
        'authority': 'payup.video',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
        'origin': 'https://payup.video',
        'referer': 'https://payup.video/tasks/video/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': us,
    }

    data = {
        'type': 'video',
    }
    response = requests.post(
        'https://payup.video/tasks/control/get.php', headers=headers, data=data).text
    response_dict = json.loads(response)
    return response_dict['data']
