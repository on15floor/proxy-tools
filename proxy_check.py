from proxy_utils import *
from utils import *

proxies = read_proxies('source.txt')
proxy_type = 'http'
proxy_manager = ProxyManager(proxy_type)

l = []
pb = ProgressBar()
pb.work_in_ide = False
pb.total = len(proxies)

for proxy in proxy_manager.check_anonymity_parallel(proxies, 50):
    pb.current = proxies.index(proxy)
    pb.good += 1
    pb.draw()
    l.append(proxy)

write_proxies('proxy_{}.txt'.format(proxy_type), l)
notify('[{}] Finished'.format(__file__))