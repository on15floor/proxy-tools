from bs4 import BeautifulSoup
import requests
from setuptools.compat import unicode
from proxy_utils import parse_proxy


def grab_proxies():
    response = requests.get("http://proxylife.org/proxy/")
    html = BeautifulSoup(response.text)
    return parse_proxy(unicode(html))