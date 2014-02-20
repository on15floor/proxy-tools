from bs4 import BeautifulSoup
import requests


def grab_proxies():


    response = requests.get("http://www.ip-adress.com/proxy_list/?k=type")
    html = BeautifulSoup(''.join(response.text))
    tag_proxies = html.findAll("a")
    proxies = []
    for i in range(0, tag_proxies.__len__()):
        if 'Proxy_Details' in tag_proxies[i].attrs['href']:
            proxy = tag_proxies[i].attrs['href'].split('/')[2]
            proxies += ['{}:{}'.format(proxy.split(':')[0], proxy.split(':')[1])]

    return proxies