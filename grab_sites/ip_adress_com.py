from bs4 import BeautifulSoup
import requests


def grab_proxies():
    response = requests.get("http://www.ip-adress.com/proxy_list/?k=type")
    html = BeautifulSoup(''.join(response.text), features="html.parser")
    tag_proxies = html.findAll("a")
    proxies = []
    for i in range(0, len(tag_proxies)):
        if 'ipv4' in tag_proxies[i].attrs['href']:
            proxy_ip = tag_proxies[i].next
            proxy_port = tag_proxies[i].nextSibling
            proxies += [f'{proxy_ip}:{proxy_port}']
    return proxies
