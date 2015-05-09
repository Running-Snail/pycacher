from storage import Storage
from ConfigParser import RawConfigParser
import json
import os


class KeyExistsError(Exception):
    def __init__(self):
        super(KeyExistsError, self).__init__()


class FileStorage(object):
    """docstring for FileStorage"""
    def __init__(self, filepath):
        super(FileStorage, self).__init__()
        self.filepath = filepath
        self.filetype = 'ini'
        self.__cp = RawConfigParser()
        self.__cp.read(self.filepath)
        self.__section = 'data'
        if not os.path.isfile(self.filepath):
            with open(self.filepath, 'w') as f:
                self.__cp.add_section(self.__section)
                self.__cp.write(f)

    def __flush(self):
        with open(self.filepath, 'w') as f:
            self.__cp.write(f)

    def insert(self, key, data):
        if self.__cp.get(self.__section, key):
            raise KeyExistsError()
        if isinstance(data, dict):
            data = json.dumps(data)
        self.__cp.set(self.__section, key, data)
        self.__flush()

    def delete(self, key):
        self.__cp.remove_option(self.__section, key)
        self.__flush()

    def find(self, key, to_json=False):
        try:
            data = self.__cp.get(self.__section, key)
        except:
            data = None
        if not data:
            return {}
        if to_json:
            try:
                return json.loads(data)
            except ValueError:
                print('cannot decode data')
                print(data)
        return data

    def update(self, key, data):
        if isinstance(data, dict):
            data = json.dumps(data)
        self.__cp.set(self.__section, key, data)
        self.__flush()

    def upsert(self, key, data):
        if isinstance(data, dict):
            data = json.dumps(data)
        self.__cp.set(self.__section, key, data)
        self.__flush()
