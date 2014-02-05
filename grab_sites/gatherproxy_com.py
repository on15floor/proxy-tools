import urllib
from bs4 import BeautifulSoup
import requests


def grab():
    response = requests.get("http://gatherproxy.com/ru/subscribe/login")
    session_id_key = 'ASP.NET_SessionId'
    session_id_value = response.cookies[session_id_key]

    html = BeautifulSoup(response.text)
    question = html.find("span", {"class": "blue"})
    captcha = ask_google(question)

    data = {
        'Username': 'on15filip@gmail.com',
        'Password': 'SP)#bjq_',
        'Captcha': captcha
    }
    headers = {
        'Content_Type': 'application/x-www-form-urlencoded'
    }
    cookies = {
        session_id_key: session_id_value
    }
    response = requests.post("http://gatherproxy.com/ru/subscribe/login",
                             data=data, headers=headers, cookies=cookies, allow_redirects=True)

    if 'Logout' not in response.text:
        raise Exception('[e]Can\'t Login')
    if 'LOGIN' not in response.text:
        print('[e]Login success, Start grab')

    html = BeautifulSoup(response.text)
    link = html.select('a[href^="/proxylist/downloadproxylist/?sid="]')[0]['href']
    sid = link.split('=')[1]

    data = {
        'ID': sid
    }
    response = requests.post("http://gatherproxy.com" + link,
                             data=data, headers=headers, cookies=cookies, allow_redirects=False)

    return response.text


def ask_google(question):
    print(question)
    g_search = urllib.parse.quote_plus(question.text)
    g_search = g_search.replace('multiplied', '*')

    response = requests.get("https://www.google.ru/search?q=" + g_search)
    html = BeautifulSoup(response.text)
    answer = html.find("h2", {"class": "r"}).text.split('=')[1].strip()

    print('[i]Google:' + answer)
    return answer


grab()