from datetime import datetime
import platform
import subprocess
import webbrowser


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
        return