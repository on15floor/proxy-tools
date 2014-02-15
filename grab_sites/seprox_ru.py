from io import BytesIO
import random
from zipfile import *

import requests


def grab_proxies():
    data = {
        'freeDownload': 'Скачать бесплатную версию'
    }

    headers = {
        'Content_Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post("http://seprox.ru/download.php",
                             data=data, headers=headers, allow_redirects=False)


    # with open("tmp.zip", "wb") as f:
    #     f.write(response.content)

    proxies = []

    zip_web = BytesIO(response.content)
    zip_f = ZipFile(zip_web, 'r')
    for file in zip_f.filelist:
        if 'anonymous' in file.filename:
            proxies += zip_f.open(file.filename)
    zip_f.close()

    return [proxy.decode().strip() for proxy in proxies]

def key_brute():
    while True:
        try:
            key = random_str(32)
            response = requests.get("http://seprox.ru/getProxyList.php?COUPON_CODE={}&COUNTRY=9&TYPE=2".format(key))
            if not response.text == 'ERROR_COUPON_NOT_FOUND':
                print('[+]Key: ', key)
                break
            else:
                print('[-] Key:', key, ' Error: ', response.text)
        except:
            pass


def random_str(length):
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    str = ''
    for i in range(0, length):
        str += random.choice(alpha)
    return str