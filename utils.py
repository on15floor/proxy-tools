from datetime import datetime
import webbrowser


def open_in_browser(text):
    temp_file = 'temp_{}.html'.format(datetime.now().timestamp())
    with open(temp_file, 'w') as html:
        html.write(text)
    webbrowser.open_new_tab(temp_file)
