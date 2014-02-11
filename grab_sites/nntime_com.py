from bs4 import BeautifulSoup
import requests


def grab_page(num_page):
    page = str(num_page).zfill(2)
    response = requests.get("http://nntime.com/proxy-updated-{}.htm".format(page))
    html = BeautifulSoup(response.text)
    tag_proxies = html.findAll("tr", {"class": "odd"})

    return


def grab_proxies():
    proxies = []

    for i in range(1, 2):
        print('[i]->Nntime.com page: {}'.format(i))
        proxies += grab_page(i)

    return proxies

print(grab_proxies())