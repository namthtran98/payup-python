import sys
import os
from twocaptcha import TwoCaptcha
import requests


def TGSolveCaptcha(siteKey, url, apikey):
    status1 = False
    while status1 == False:
        responseGetIdGooleKey = requests.get(
            f"http://goodxevilpay.pp.ua/in.php?key={apikey}&pageurl={url}?level=middle&method=userrecaptcha&googlekey={siteKey}")
        outputGoogleKey = responseGetIdGooleKey.text
        if "|" not in outputGoogleKey:
            continue
        id = outputGoogleKey.split("|")[1]
        statusGoogleKey = outputGoogleKey.split("|")[0]
        if statusGoogleKey == "OK":
            status1 = True
    status2 = False
    while status2 == False:
        response = requests.get(
            f"http://goodxevilpay.pp.ua/res.php?key={apikey}&action=get&id={id}")
        output = response.text
        if "|" not in output:
            continue
        code = output.split("|")[1]
        status = output.split("|")[0]
        if status == "OK":
            status2 = True

    return code
