from bs4 import BeautifulSoup
import requests


def get_delimiter(delimiter_trash):
    delimiter_list = []
    for i in range(0, delimiter_trash.__len__()):
        delimiter_list += [delimiter_trash[i][-6:-4]]

    frequency, delimiter = 0, 0
    for d in delimiter_list:
        c = delimiter_list.count(d)
        if c > frequency:
            frequency, delimiter = c, d

    return delimiter


def grab_page(num_page):
    proxies = []
    proxy_ip = []
    proxy_port = []
    page = str(num_page).zfill(2)
    response = requests.get("http://nntime.com/proxy-updated-{}.htm".format(page))

    html = BeautifulSoup(response.text, features="html.parser")
    tag_proxy_ip_odd = html.findAll("tr", {"class": "odd"})
    tag_proxy_ip_even = html.findAll("tr", {"class": "even"})
    tag_proxy_port = html.findAll("input", {"type": "checkbox"})
    proxy_amount = tag_proxy_port.__len__()
    o, e = 0, 0
    for i in range(0, proxy_amount):
        if i % 2 == 0:
            proxy_ip += [tag_proxy_ip_odd[o].text.split('\n')[0]]
            o += 1
            proxy_port += [tag_proxy_port[i].attrs['value']]
        else:
            proxy_ip += [tag_proxy_ip_odd[o].text.split('\n')[0]]
            e += 1
            proxy_port += [tag_proxy_port[i].attrs['value']]

    delimiter = get_delimiter(proxy_port)
    for i in range(0, proxy_amount):
        proxies += [f'{proxy_ip[i]}:{proxy_port[i].split(delimiter)[1]}']

    return proxies


def grab_proxies(number_of_page=15):
    proxies = []
    for i in range(1, number_of_page):
        print(f'[i]->Nntime.com page: {i}')
        proxies += grab_page(i)

    return proxies
