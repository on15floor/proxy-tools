from io import BytesIO
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