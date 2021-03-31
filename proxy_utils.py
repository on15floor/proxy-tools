import re
import itertools
import requests
from silent_threading import SilentThreadPool
from utils import *


def read_proxies(file_path):
    with open(file_path) as f:
        lines = (line.strip() for line in f.readlines())
        lines = (line.split(':') for line in lines if line)
        lines = (line for line in lines if line[0] and len(line) == 2)
        lines = (first(v) for k, v in itertools.groupby(sorted(lines), lambda p: p[0]))
        return [line[0] + ':' + line[1] if line[1] else line[0] + ':8080' for line in lines]


def check_anonymity_http(proxy, timeout=3):
    proxies = {"http": "http://{}".format(proxy)}
    response = requests.get("http://checkip.amazonaws.com", proxies=proxies, timeout=timeout)
    if response.status_code != 200:
        print(f'[-]{proxy}')
        raise SilentException('Bad proxy')
    if response.text.strip() != proxy.split(':')[0]:
        print(f'[-]{proxy}')
        raise SilentException('Bad anonymity')
    else:
        print(f'[+]{proxy}')
    return proxy


def check_anonymity_https(proxy, timeout=3):
    proxies = {"https": "https://{}".format(proxy)}
    response = requests.get("https://wtfismyip.com/text", proxies=proxies, verify=False, timeout=timeout)
    if response.status_code != 200:
        raise SilentException('Bad proxy')
    if response.text.strip() != proxy.split(':')[0]:
        raise SilentException('Bad anonymity')
    return proxy


class ProxyManager:
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
            raise SilentException('Choose type of proxy first')


def parse_proxies(text: str) -> list:
    return re.findall('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,4})', text, re.DOTALL)
