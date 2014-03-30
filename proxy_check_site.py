import requests
from proxy_utils import parse_proxy
from utils import *

sites = read_list('sites.txt')
proxies = []
proxy_count = 0
sites_good = []
for site in sites:
        print('[i]Site:{}'.format(site))
        try:
            proxies_from_site = parse_proxy(requests.get(site, timeout=5).text)
            if len(proxies_from_site) != 0:
                proxies += proxies_from_site
                proxy_count += len(proxies_from_site)
                sites_good.append(site)
                print('{}Proxy from site:{}, Total:{}'.format(bold(color('32', str('[+]'))),
                                                              str(len(proxies_from_site)).zfill(5),
                                                              str(proxy_count).zfill(5)))
            else:
                print('{}: {}'.format(bold(color('31', str('[-]No proxy from:'))), site))
        except:
            print('{}: {}'.format(bold(color('31', str('[-]Dead Site:'))), site))

write_list_w('sites_good.txt', sites_good)
notify('[{}] Finished'.format(__file__))