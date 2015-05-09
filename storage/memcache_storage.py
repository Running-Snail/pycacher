from storage import Storage
import memcache


class MemcachedStorage(object):
    """docstring for MemcachedStorage"""
    def __init__(self, addrs):
        super(MemcachedStorage, self).__init__()
        self.addrs = addrs
        self.__mem = memcache.Client(addrs)

    def insert(self, key, data):
        self.__mem.set(key, data)

    def delete(self, key):
        self.__mem.delete(key)

    def find(self, key):
        return self.__mem.get(key)

    def update(self, key, data):
        self.__mem.set(key, data)

    def upsert(self, key, data):
        self.__mem.set(key, data)
