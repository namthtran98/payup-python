import requests
import json
from time import sleep
import re
from solveClickCapcha import solveClickCapcha

cookie1 = input('Nhap cookie payup.video:')
us = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"


def payup_video(cookie, us):
    # Lay job
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
    if int(data3['limitHour']) == 0 and int(data3['cnt']) <= 700:
        print('het job')
        sleep(20)
        return (payup_video)
    elif int(data3['limitHour']) >= 0 and int(data3['cnt']) == 0:
        print('da chay het 700 job')
        sleep(60)
        return (payup_video)
    else:
        # time_job = response_dict['data']['duration']
        link_job = response_dict['data']['href']
        link_job2 = link_job.replace(
            'https://trustspace.squarespace.com/view?v=', '')
        data_job = 'data='+link_job2
        s_id = response_dict['data']['s_id']
        # print(data_job)

        # start job

        # data_start = data_job,

        response99 = requests.post(
            'https://payup.video/tasks/control/start.php', headers=headers, data=data_job).json
        # print(response)

        # sleep(int(time_job))

        # nhan job (get.php)

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
        }

        response2 = requests.post(
            'https://payup.video/captcha/control/get.php', headers=headers2, data=data2)

        if response2.status_code == 200:
            rs_load = response2.json()
            co_captcha_khong = rs_load['access']
            if False == co_captcha_khong:
                print('dinh captcha')
                body = rs_load['data']
                g = giai_captcha(s_id=s_id, headers2=headers2)

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

        # sleep(2)


def giai_captcha(s_id, headers2):
    result = solveClickCapcha()
    txt = result['code']
    txtSpilit = re.split("coordinates\:x=(\d*),y=(\d*)", txt)
    x = txtSpilit[1]
    y = txtSpilit[2]

    print(x, y)

    data_giai = {
        'x': x,
        'y': y,
        's_id': s_id,
    }

    response5 = requests.post(
        'https://payup.video/captcha/control/check.php', headers=headers2, data=data_giai).json()
    status = str(response5.get('status'))
    body = response5.get('data')
    if status == "data":
        return giai_captcha(s_id, headers2)
    else:
        print(response5)
        print("giai thanh cong")


while True:
    payup = payup_video(cookie=cookie1, us=us)

    print(payup)
