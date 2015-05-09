import threading
import time


class CacheListener(object):
    """docstring for CacheListener"""
    def __init__(self):
        super(CacheListener, self).__init__()
        self.cacher = None

    def notify(self, name, cached_data):
        raise NotImplementedError()


class Cacher(threading.Thread):
    """docstring for Cacher"""
    name = 'cacher'

    def __init__(self):
        super(Cacher, self).__init__()
        self.listeners = []
        self.cached_data = None
        self.cached_time = 0
        self.expires_in = 1
        self.running = True

    def stop(self):
        self.running = False

    def update(self):
        raise NotImplementedError()

    def run(self):
        while self.running:
            self.cached_data, self.expires_in = self.update()
            self.on_update(self.cached_data)
            self.cached_time = int(time.time())
            time.sleep(self.expires_in)

    def start_cache(self):
        self.start()

    def add_listener(self, l):
        l.cacher = self
        self.listeners.append(l)

    def on_update(self, cached_data):
        for l in self.listeners:
            try:
                l.notify(self.name, cached_data)
            except (AttributeError, NotImplementedError):
                pass
