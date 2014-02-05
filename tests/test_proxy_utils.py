from datetime import datetime
import os
from tempfile import gettempdir
from unittest import TestCase

from proxy_utils import read_proxies


class TestReadProxies(TestCase):
    def test_read_proxies(self):
        proxies = [
            '192.168.1.1:80',
            ':80',
            '192.168.1.3:',
            '',
            '192.168.1.1:92'
        ]
        expected = [
            '192.168.1.1:80',
            '192.168.1.3:8080'
        ]
        file = os.path.join(gettempdir(), str(datetime.now().timestamp()) + '.tmp')
        with open(file, 'w') as f:
            f.write('\n'.join(proxies))
        result = read_proxies(file)
        os.remove(file)
        self.assertEqual(expected, sorted(result))