import sys
import time


def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"


def bold(msg):
    return u'\033[1m%s\033[0m' % msg


def progress_bar(current, total):
    bar_size = 50
    amount = int(current / (total / float(bar_size)))
    remain = bar_size - amount
    bar = '{}\{}'.format('=' * amount, '.' * remain)
    percent = str((total*current)/100).zfill(2)
    sys.stdout.write('\rProgress: {}% [{}] {}/{}'.format(color('32', percent), bar, bold(current), bold(total)))
    sys.stdout.flush()


NUM = 100
for i in range(NUM + 1):
    progress_bar(i, NUM)
    time.sleep(0.05)