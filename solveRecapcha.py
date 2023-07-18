import sys
import os
from twocaptcha import TwoCaptcha
import requests


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
