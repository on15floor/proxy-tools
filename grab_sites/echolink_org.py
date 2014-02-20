from bs4 import *
import requests


def grab_proxies():
    response = requests.get("http://www.echolink.org/proxylist.jsp")
    html = BeautifulSoup(''.join(response.text))
    tag_proxies = html.findAll("tr")
    proxies = []
    for i in range(3, tag_proxies.__len__()):
        if 'Ready' in tag_proxies[i].text:
            proxies += [
                '{}:{}'.format(tag_proxies[i].text.split('\n')[2].strip(), tag_proxies[i].text.split('\n')[3]).strip()]

    return proxies