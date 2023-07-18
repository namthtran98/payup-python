from solveClickCapcha import giai_captcha
import requests
import json
import time


def SolvePayupCaptcha(us, apikey, cookie):
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
    data3 = response_dict['data']
    s_id = response_dict['data']['s_id']
    id = response_dict['data']['id']
    headers2 = {
        'authority': 'payup.video',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://trustspace.squarespace.com',
        'referer': 'https://trustspace.squarespace.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': us,
    }

    data2 = {
        's_id': s_id,
        'id': id
    }

    response2 = requests.post(
        'https://payup.video/captcha/control/get.php', headers=headers2, data=data2)
    if response2.status_code == 200:
        rs_load = response2.json()
        co_captcha_khong = rs_load['status']
        if "ok" == co_captcha_khong:
            print('dinh captcha')
            body = rs_load['data']
            g = giai_captcha(apikey=apikey, body=body,
                             s_id=s_id, headers2=headers2)

            # if response5.status_code == 200:
            #     print('giai captcha thanh cong')
            # else:
            #     return "GIAI CAPTCHA LOI"

        else:
            headers = {
                'authority': 'payup.video',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://trustspace.squarespace.com',
                'referer': 'https://trustspace.squarespace.com/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': us,
            }

            data = {
                's_id': s_id,
            }

            response3 = requests.post(
                'https://payup.video/captcha/control/check.php', headers=headers, data=data)

            print(response3)
