from bs4 import BeautifulSoup
import requests
from proxy_utils import parse_proxy


def grab_page(num_page):
    page = str(num_page).zfill(2)
    response = requests.get("http://www.samair.ru/proxy/proxy-{}.htm".format(page))
    html = BeautifulSoup(response.text)
    div = html.find("div", {"id": "ipportonly"})
    link = div.contents[3].attrs.get('href')
    text = requests.get("http://www.samair.ru" + link).text
    return parse_proxy(text)


def grab_proxies():
    proxies = []

    for i in range(1, 31):
        print('[i]->Samair.ru page: {}'.format(i))
        proxies += grab_page(i)

    return proxies