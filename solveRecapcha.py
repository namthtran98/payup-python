import sys
import os
from twocaptcha import TwoCaptcha
import requests


def solveRecapcha(siteKey, url):
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', '9eb41b119c979f57c678ff410eb14d1d')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=siteKey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result


def TGSolveCaptcha(siteKey, url, apikey):
    responseGetIdGooleKey = requests.get(
        f"http://goodxevilpay.pp.ua/in.php?key={apikey}&pageurl={url}?level=middle&method=userrecaptcha&googlekey={siteKey}")
    outputGoogleKey = responseGetIdGooleKey.text
    if "|" not in outputGoogleKey:
        return "FAIL"
    id = outputGoogleKey.split("|")[1]
    response = requests.get(
        f"http://goodxevilpay.pp.ua/res.php?key={apikey}&action=get&id={id}")
    output = response.text
    if "|" not in output:
        return "FAIL"
    code = output.split("|")[1]
    return code
