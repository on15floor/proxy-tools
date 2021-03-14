import os
import platform
import subprocess
import webbrowser
import time


def first(iterable):
    for item in iterable:
        return item
    raise ValueError('No satisfactory value found')


def open_in_browser(text):
    temp_file = 'temp_{}.html'.format(time.time())
    with open(temp_file, 'w') as html:
        html.write(text)
    webbrowser.open_new_tab(temp_file)


def notify(message):
    if 'Ubuntu' in str(platform.dist()):
        subprocess.Popen(['notify-send', message])
        os.system("/usr/bin/canberra-gtk-play --id='message'")
    if 'LinuxMint' in str(platform.dist()):
        subprocess.Popen(['notify-send', message])


def read_list(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines()]


def write_list_a(file: str, some_list: list):
    if len(some_list) != 0:
        with open(file, 'a') as f:
            f.write('\n'.join(some_list))
    else:
        print('[e]List is Nool')


def write_list_w(file: str, some_list: list):
    if len(some_list) != 0:
        with open(file, 'w') as f:
            f.write('\n'.join(some_list))
    else:
        print('[e]List is Nool')