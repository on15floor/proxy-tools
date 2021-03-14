from bs4 import *
import requests


def grab_proxies():
    response = requests.get("http://www.echolink.org/proxylist.jsp")
    html = BeautifulSoup(''.join(response.text), features="html.parser")
    proxies_tag = html.findAll("tr")
    proxies = []
    for i in range(3, len(proxies_tag)):
        if 'Ready' in proxies_tag[i].text:
            proxies_tag_trash = proxies_tag[i].text.split('\n')
            proxie_ip = proxies_tag_trash[2].strip()
            proxie_port = proxies_tag_trash[3].strip()
            proxies.append(f'{proxie_ip}:{proxie_port}')
    return proxies
