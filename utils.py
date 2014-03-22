from datetime import datetime
import os
import platform
import subprocess
import webbrowser
import sys


def first(iterable):
    for item in iterable:
        return item
    raise ValueError('No satisfactory value found')


def open_in_browser(text):
    temp_file = 'temp_{}.html'.format(datetime.now().timestamp())
    with open(temp_file, 'w') as html:
        html.write(text)
    webbrowser.open_new_tab(temp_file)


def notify(message):
    if 'Ubuntu' in str(platform.dist()):
        subprocess.Popen(['notify-send', message])
        os.system("/usr/bin/canberra-gtk-play --id='message'")
    if 'LinuxMint' in str(platform.dist()):
        subprocess.Popen(['notify-send', message])


def color(this_color, string):
    return "\033[{}m{}\033[0m".format(this_color, string)


def bold(msg):
    return u'\033[1m%s\033[0m' % msg


def progress_bar(current, total, good):
    bar_size = 50
    amount = int(current / (total / float(bar_size)))
    remain = bar_size - amount
    bar = '{}\{}'.format('=' * amount, '.' * remain)
    bad = current - good
    sys.stdout.write('\rProgress:  {}/{} [{}] Good: {} Bad: {}'.format(bold(current),
                                                                       bold(total),
                                                                       bar,
                                                                       bold(color('32', str(good))),
                                                                       bold(color('31', str(bad)))))
    sys.stdout.flush()