from proxy_utils import *
from utils import notify

l = []
proxies = read_proxies('source.txt')
proxy_type = 'http'
proxy_manager = ProxyManager(proxy_type)

for proxy in proxy_manager.check_anonymity_parallel(proxies, 50):
    print(proxy)
    l.append(proxy)

write_proxies('proxy_{}.txt'.format(proxy_type), l)
notify('[{}] Finished'.format(__file__))