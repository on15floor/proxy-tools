import datetime
import os
import platform
import subprocess
import webbrowser
import sys
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


def color(this_color, string):
    return "\033[{}m{}\033[0m".format(this_color, string)


def bold(msg):
    return u'\033[1m%s\033[0m' % msg


class ProgressBar():
    def __init__(self):
        self.current = 0
        self.total = 0
        self.good = 0
        self.start_time = time.time()
        self.bar_size = 30

    def draw(self):
        amount = int(self.current / (self.total / float(self.bar_size)))
        remain = self.bar_size - amount

        current = str(self.current).zfill(len(str(self.total)))
        bar = '{}>{}'.format('=' * amount, '.' * remain)
        bad = str(self.current - self.good).zfill(len(str(self.total)))
        good = str(self.good).zfill(len(str(self.total)))
        time_exec = int(time.time()-self.start_time)
        if self.current != 0:
            time_total = int((self.total*time_exec)/self.current)
        else:
            time_total = 999
        time_remaining = time_total-time_exec
        sys.stdout.write("\r")
        sys.stdout.write('Progress: {}/{} [{}] Good: {} Bad: {} |TIME Exec: {} Remaining: {}|'.format(
            bold(current),
            bold(self.total),
            bar,
            bold(color('32', str(good))),
            bold(color('31', str(bad))),
            bold(color('34', str(datetime.timedelta(seconds=time_exec)))),
            bold(color('33', str(datetime.timedelta(seconds=time_remaining)))),
        ))
        sys.stdout.flush()


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