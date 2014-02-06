import random
import requests


def grab_proxies():
    print('[i]Grab hideme.ru:')
    for i in range(1, 4):
        key = random.randint(100000, 999999)

        data = {
            'c': key
        }
        headers = {
            'Content_Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post("http://hideme.ru/login",
                                 data=data, headers=headers, allow_redirects=False)

        if response.status_code == 302:
            proxies = requests.get("http://hideme.ru/api/proxylist.txt?out=plain&lang=ru")
            print('[+]Hideme.ru key: ' + str(key))
            return [proxy for proxy in proxies.content.decode().split('\r\n')]
        else:
            if i == 3:
                print('[-]Hideme.ru: Key not found')