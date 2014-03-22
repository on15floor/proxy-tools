from proxy_utils import *
from utils import *

proxies = read_proxies('source.txt')
proxy_type = 'http'
proxy_manager = ProxyManager(proxy_type)

l = []
good_proxies = 0
pb = ProgressBar()
pb.total = len(proxies)

for proxy in proxy_manager.check_anonymity_parallel(proxies, 50):
    good_proxies += 1
    pb.current = proxies.index(proxy)
    pb.good = good_proxies
    pb.draw()
    l.append(proxy)

write_proxies('proxy_{}.txt'.format(proxy_type), l)
notify('[{}] Finished'.format(__file__))