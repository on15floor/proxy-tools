from proxy_utils import *

proxies = read_proxies('source.txt')
proxy_manager = ProxyManager()

l = []

for proxy in proxy_manager.check_anonymity_parallel(proxies, 50):
    print(proxy)
    l.append(proxy)

write_proxies('proxy.txt', l)