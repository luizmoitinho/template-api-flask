from src.config.config import Config

class ServoModel:
    def __init__(self, pan, tilt):
        self.__pan = pan
        self.__tilt = tilt
        self.__conf = Config().config
        
    def set_pan(self, pan):
        if pan > self.__conf['servo']['max_degree_pan'] or pan < self.__conf['servo']['min_degree_pan']:
            return None
        self.__pan = pan

    def set_tilt(self, tilt):
        if tilt > self.__conf['servo']['max_degree_tilt'] or pan < self.__conf['servo']['min_degree_tilt']:
            return None
        self.__pan = tilt
    
    def get_pan(self):
        return self.__pan

    def get_tilt(self):
        return self.__tilt
