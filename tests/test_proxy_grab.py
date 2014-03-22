import datetime
import sys
import time


def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"


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
        sys.stdout.write('Progress: {}/{} [{}] Good: {} Bad: {} |Runtime: {} Remaining: {}|'.format(
            bold(current),
            bold(self.total),
            bar,
            bold(color('32', str(good))),
            bold(color('31', str(bad))),
            bold(color('34', str(datetime.timedelta(seconds=time_exec)))),
            bold(color('33', str(datetime.timedelta(seconds=time_remaining)))),
        ))
        sys.stdout.flush()


NUM = 100
p = ProgressBar()
p.total = NUM
p.good = 2

for i in range(NUM + 1):
    p.current = i
    p.draw()
    time.sleep(0.05)