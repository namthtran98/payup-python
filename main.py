import requests
import json
from time import sleep
import re

cookie1 = "_ga=GA1.1.1699602678.1685788762; _ym_d=1685788763; _ym_uid=1685788763665220976; newUser=1; PHPSESSID=fgmvg022t4o28ds07epsh8vkvu; signed=1; hash=ed73e7d462472e41b1a9e67ce3fc886a; _ym_isad=1; _ym_visorc=b; _ga_5JGWQMNX26=GS1.1.1687322375.26.1.1687322591.0.0.0"
apikey1 = "o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42"
us = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"


# so_luong = 4
# Thread = []

def giai_captcha(apikey, body, s_id, headers2):
    apikey = apikey
    body = body
    coordinates = take_image(apikey=apikey, body=body)

    if coordinates == "FAIL":
        print("SEVER captcha loi hoac update")
    else:
        toa_do_x = coordinates[0]
        toa_do_y = coordinates[1]

    # print(captcha_id)
    # sleep(1)
    # response2 = requests.get('http://goodxevilpay.shop/res.php?key='+apikey+'&id='+captcha_id).text
    # toa_do_x = response2.split("x=")[1].split(",y=")[0]
    # toa_do_y = response2.split("y=")[1]

    print(toa_do_x, toa_do_y)

    data_giai = {
        'x': toa_do_x,
        'y': toa_do_y,
        's_id': s_id,
    }

    response5 = requests.post(
        'https://payup.video/captcha/control/check.php', headers=headers2, data=data_giai).json()
    status = str(response5.get('status'))
    body = response5.get('data')
    if status == "data":
        # hi = giai_captcha_lai(apikey=apikey,base64_lan2a=base64_lan2,s_id=s_id,headers2=headers2)
        return giai_captcha(apikey, body, s_id, headers2)
    # def giai_captcha_lai(base64_lan2a):

    #     response6 = requests.post("http://goodxevilpay.shop/in.php",files=(('method', (None, "buxmoney")),('key', (None, apikey)),('body', (None, base64_lan2)),))
    #     output2 = response6.text
    #     captcha_id2 = output2.split("|")[1]
    #     print(captcha_id2,"giai lai")
    #     sleep(4)
    #     response7 = requests.get('http://goodxevilpay.shop/res.php?key='+apikey+'&id='+captcha_id2).text
    #     toa_do_x2 = response7.split("x=")[1].split(",y=")[0]
    #     toa_do_y2 = response7.split("y=")[1]
    #     print(toa_do_x2,toa_do_y2)

    #     data_giai2 = {
    #         'x': toa_do_x2,
    #         'y': toa_do_y2,
    #         's_id': s_id,
    #     }

    #     response8 = requests.post('https://payup.video/captcha/control/check.php', headers=headers2, data=data_giai2).json()
    #     status2 = str(response8.get('status'))
    #     if status2 == "data":
    #         base64_lan2b = response8.get('data')
    #         return giai_captcha_lai(base64_lan2a=base64_lan2b)
    #     else:
    #         break

    else:
        print(response5)
        print("giai thanh cong")


def take_image(apikey, body):
    response = requests.post(
        "http://goodxevilpay.shop/in.php",
        files=(
            ('method', (None, "buxmoney")),
            ('key', (None, apikey)),
            ('body', (None, body)),
        )
    )
    output = response.text
    if "|" not in output:
        return "FAIL"
    captcha_id = output.split("|")[1]

    index = 0
    output = "CAPCHA_NOT_READY"
    while output == "CAPCHA_NOT_READY":
        index += 1
        if index >= 20:
            return "FAIL"
        sleep(1)
        response = requests.get(
            f"http://goodxevilpay.shop/res.php?key={apikey}&id={captcha_id}")
        output = response.text

    if "coordinate:" not in output:
        return "FAIL"
    output = output.split("coordinate:")[1]
    numbers = re.findall(r'\d+', output)
    if len(numbers) != 2:
        return "FAIL"

    return numbers


# def giai_captcha_lai(apikey,base64_lan2a,s_id,headers2):

#     response6 = requests.post("http://goodxevilpay.shop/in.php",files=(('method', (None, "buxmoney")),('key', (None, apikey)),('body', (None, base64_lan2a)),))
#     output2 = response6.text
#     captcha_id2 = output2.split("|")[1]
#     print(captcha_id2,"giai lai")
#     sleep(4)
#     response7 = requests.get('http://goodxevilpay.shop/res.php?key='+apikey+'&id='+captcha_id2).text
#     toa_do_x2 = response7.split("x=")[1].split(",y=")[0]
#     toa_do_y2 = response7.split("y=")[1]
#     print(toa_do_x2,toa_do_y2)

#     data_giai2 = {
#         'x': toa_do_x2,
#         'y': toa_do_y2,
#         's_id': s_id,
#     }


#     response8 = requests.post('https://payup.video/captcha/control/check.php', headers=headers2, data=data_giai2).json()
#     status2 = str(response8.get('status'))
#     if status2 == "data":
#         base64_lan2a = response8.get('data')
#         return giai_captcha_lai(apikey,base64_lan2a,s_id,headers2)
#     elif status2 == 'ok':
#         print('giai captcha lai thanh cong')
def payup_video(cookie, apikey, us):
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

        # sleep(2)


while True:
    payup1 = payup_video(cookie=cookie1, apikey=apikey1, us=us)
    print(payup1)
# f = tool()
# for i in f:
#     i = f.start()
#     print("HI")
# f = tool()
# c = tool().start()
# thread1 = Thread(target = c)
# thread1.start()
# sleep(2)
# thread2 = Thread(target = c)
# thread2.start()


# for i in range(so_luong):
#     f = tool(i)
#     f.start
