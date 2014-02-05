from bs4 import BeautifulSoup
import requests
from proxy_utils import proxy_grab


def grab_page(num_page):
    page = str(num_page).zfill(2)
    response = requests.get("http://www.samair.ru/proxy/proxy-{}.htm".format(page))
    html = BeautifulSoup(response.text)
    div = html.find("div", {"id": "ipportonly"})
    link = div.contents[3].attrs.get('href')
    return proxy_grab("http://www.samair.ru" + link)


def grab():
    print('[i]Grab samir.ru...')
    proxies = []

    for i in range(1, 31):
        print('[i]Grab samir.ru [Page: {}]'.format(i))
        proxies += grab_page(i)

    return proxies