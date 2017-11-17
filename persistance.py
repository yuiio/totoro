import os, dill
from functools import wraps

config_file = 'user_data.dill'

class User():    
    
    def __init__(self):
        self.init()
        if os.path.exists(config_file):
            self.load()

    def init(self):
        self.__dict__ = {}
        self.name = 'elliot'
        self.password = 'splitaine'
        self.logged = False
        self.map_unlocked = False
        self.level = 0
        self.reps = {}

    def save(self):
        with open(config_file, 'wb') as f:
            dill.dump(self, f)
        
    def load(self):
        with open(config_file, 'rb') as f:
            user = dill.load(f)
        self.__dict__ = user.__dict__

