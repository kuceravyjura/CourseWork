import shelve
from Parameters import *

class Save:
    def __init__(self):
        self.file = shelve.open('data')

    def get(self, name):
        try:
            return self.file[name]
        except:
            pass

    def save(self, name, value):
        self.file[name] = value

    def __del__(self):
        self.file.close()


