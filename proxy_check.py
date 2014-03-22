from proxy_utils import *
from utils import *

l = []
good_proxies = 0
proxies = read_proxies('source.txt')
proxy_type = 'http'
proxy_manager = ProxyManager(proxy_type)

for proxy in proxy_manager.check_anonymity_parallel(proxies, 50):
    good_proxies += 1
    progress_bar(proxies.index(proxy), len(proxies), good_proxies)
    l.append(proxy)

write_proxies('proxy_{}.txt'.format(proxy_type), l)
notify('[{}] Finished'.format(__file__))