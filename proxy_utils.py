import re
import itertools
import requests
from silent_threading import SilentThreadPool
from utils import first


def read_proxies(file_path):
    with open(file_path) as f:
        lines = (line.strip() for line in f.readlines())
        lines = (line.split(':') for line in lines if line)
        lines = (line for line in lines if line[0] and len(line) == 2)
        lines = (first(v) for k, v in itertools.groupby(sorted(lines), lambda p: p[0]))
        return [line[0] + ':' + line[1] if line[1] else line[0] + ':8080' for line in lines]


def write_proxies(file_path: str, proxies):
    with open(file_path, 'w') as f:
        f.write('\n'.join(proxies))


class ProxyException(Exception):
    pass


def check_anonymity_http(proxy, timeout=3):
    proxies = {"http": "http://{}".format(proxy)}
    response = requests.get("http://fh7915ko.bget.ru/ip.php", proxies=proxies, timeout=timeout)
    if response.status_code != 200:
        raise ProxyException('Bad proxy')
    if response.text != proxy.split(':')[0]:
        raise ProxyException('Bad anonymity')
    return proxy


def check_anonymity_https(proxy, timeout=1):
    proxies = {"https": "https://{}".format(proxy)}
    response = requests.get("https://wtfismyip.com/text", proxies=proxies, timeout=timeout)
    if response.status_code != 200:
        raise ProxyException('Bad proxy')
    if response.text.strip() != proxy.split(':')[0]:
        raise ProxyException('Bad anonymity')
    return proxy


class ProxyManager():
    def __init__(self, proxy_type):
        self._executor = None
        self.proxy_type = proxy_type

    def check_anonymity_parallel(self, proxies, max_workers=4):
        if self.proxy_type == 'http':
            with SilentThreadPool(max_workers) as self._executor:
                for result in self._executor.map(check_anonymity_http, proxies):
                    if result:
                        yield result
        elif self.proxy_type == 'https':
            with SilentThreadPool(max_workers) as self._executor:
                for result in self._executor.map(check_anonymity_https, proxies):
                    if result:
                        yield result
        else:
            raise ProxyException('Choose type of proxy first')

    def stop(self, wait=False):
        if self._executor:
            self._executor.shutdown(wait=wait)


def parse_proxy(text: str) -> list:
    return re.findall('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,4})', text, re.DOTALL)
