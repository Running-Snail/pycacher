from cacher import CacheListener


class UpdateListener(CacheListener):
    """docstring for UpdateListener"""
    def __init__(self, storage):
        super(UpdateListener, self).__init__()
        self.__storage = storage

    def notify(self, name, cached_data):
        print('update notified by {}'.format(name))
        self.__storage.upsert(name, cached_data)


class Controller(object):
    def __init__(self, storage):
        super(Controller, self).__init__()
        self.cachers = []
        self.storage = storage
        self.listener = UpdateListener(self.storage)

    def add_cacher(self, cacher):
        self.cachers.append(cacher)
        cacher.controller = self
        cacher.add_listener(self.listener)

    def start_cache(self):
        print('start to cache')
        for c in self.cachers:
            c.start_cache()

    def get_cache(self, key):
        return self.storage.find(key)
