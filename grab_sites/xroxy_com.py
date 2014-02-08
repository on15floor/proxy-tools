from bs4 import BeautifulSoup
import requests


def grab_proxies():
    proxies = ''
    response = requests.get("http://www.xroxy.com/proxyrss.xml")
    html = BeautifulSoup(response.text)
    tag_proxies = html.findAll('prx:proxy')

    for tag_proxy in tag_proxies:
        ip = tag_proxy.findAll('prx:ip')
        port = tag_proxy.findAll('prx:port')
        proxy = ip[0].text + ':' + port[0].text + '\n'
        proxies += proxy

    return [proxy for proxy in proxies.split('\n')]