from concurrent.futures.thread import ThreadPoolExecutor


class SilentThreadPool(ThreadPoolExecutor):
    def __init__(self, max_workers):
        super().__init__(max_workers)
        self._func = None

    def map(self, func, *iterables, timeout=None):
        self._func = func
        return super().map(self._mute_exception, *iterables, timeout=timeout)

    def _mute_exception(self, *args):
        try:
            return self._func(*args)
        except:
            pass