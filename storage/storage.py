class Storage(object):
    """docstring for Storage"""
    def __init__(self):
        super(Storage, self).__init__()

    def insert(self, key, data):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()

    def find(self, key):
        raise NotImplementedError()

    def update(self, key, data):
        raise NotImplementedError()

    def upsert(self, key, data):
        raise NotImplementedError()
