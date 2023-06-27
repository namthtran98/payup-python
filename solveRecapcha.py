import sys
import os
from twocaptcha import TwoCaptcha


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
