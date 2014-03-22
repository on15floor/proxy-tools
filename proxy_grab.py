import requests
from grab_sites import gatherproxy_com, hideme_ru, samair_ru, proxy_list_org, proxylife_org, xroxy_com, seprox_ru, \
    nntime_com, ip_adress_com, echolink_org, foxtools_ru
from proxy_utils import write_proxies, parse_proxy
from utils import notify


proxy_count = 0


def full_grab():
    global proxy_count
    proxies = []
    functions = [
        hideme_ru.grab_proxies,
        samair_ru.grab_proxies,
        gatherproxy_com.grab_proxies,
        proxy_list_org.grab_proxies,
        proxylife_org.grab_proxies,
        xroxy_com.grab_proxies,
        seprox_ru.grab_proxies,
        nntime_com.grab_proxies,
        ip_adress_com.grab_proxies,
        echolink_org.grab_proxies,
        foxtools_ru.grab_proxies,
    ]

    for func in functions:
        print('[i]Site:{}'.format(func.__module__))
        try:
            result_func = func()
            if result_func:
                proxies += result_func
                proxy_count += len(result_func)
                print('[+]Proxy from site:{}, Total:{}'.format(str(len(result_func)).zfill(5),
                                                               str(proxy_count).zfill(5)))
        except Exception as e:
            print(e)
    proxies += fast_grab()

    return proxies


def fast_grab():
    global proxy_count
    proxies = []
    sites = ["http://russianproxy.ru/proxy_list_http_fastest",
             "http://chingachgook.net/servisy/proxy",
             "http://www.x-scripts.com/proxy.php",
             "http://vps.rosinstrument.com/proxy/l100.xml",
             "http://www.cybersyndrome.net/pla5.html?guid=ON",
             "http://proxy-servers.eu/",
             "http://aliveproxies.com/pages/page-scrapebox-proxies/",
             "http://www.therealist.ru/proksi/spisok-elitnyx-proksi-serverov",
             "http://ubuntu-russian.ru/microsoft.com/all-proxy-best",
             "http://notepad.cc/share/ogBPDXZhZL",
             "http://anonimsurfer.info/export/hzteam-yAMUO5uy4CKnA7Ka7cSa7k5ihMpA5a/0/s/types=http",
             "http://www.cool-tests.com/anon-elite-proxy.php",
             "http://fineproxy.org/%D1%81%D0%B2%D0%B5%D0%B6%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%BA%D1%81%D0%B8/",
             "http://www.prime-speed.ru/proxy/free-proxy-list/all-working-proxies.php",
             "http://www.shroomery.org/ythan/proxylist.php",
             "http://www.therealist.ru/proksi/spisok-anonimnyx-i-elitnyx-proksi",
             "http://www.cybersyndrome.net/pla5.html",
             "http://www.cybersyndrome.net/plr5.html",
             "http://tophacksavailable.blogspot.ru/",
             "http://www.proxylists.net/http_highanon.txt"]

    for site in sites:
        print('[i]Site:{}'.format(site))
        proxies_from_site = parse_proxy(requests.get(site).text)
        if len(proxies_from_site) != 0:
            proxies += proxies_from_site
            proxy_count += len(proxies_from_site)
            print('[+]Proxy from site:{}, Total:{}'.format(str(len(proxies_from_site)).zfill(5), str(proxy_count).zfill(5)))
        else:
            print('[-]SITE ERROR: {}'.format(site))

    return proxies


write_proxies('source.txt', full_grab())
# write_proxies('source.txt', fast_grab())
notify('[{}] Finished'.format(__file__))