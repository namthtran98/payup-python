from twocaptcha import TwoCaptcha
import os
import sys
import requests
from time import sleep
import re


def giai_captcha(apikey, body, s_id, headers2):
    apikey = apikey
    body = body
    coordinates = take_image(apikey=apikey, body=body)
    toa_do_x = ''
    toa_do_y = ''
    if coordinates == "FAIL":
        print("SEVER captcha loi hoac update")
        giai_captcha(apikey=apikey, body=body, s_id=s_id, headers2=headers2)
    else:
        toa_do_x = coordinates[0]
        toa_do_y = coordinates[1]
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
