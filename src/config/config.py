"""
Config File for enviroment variables
"""
import configparser
import toml
import os
import sys

class Config():
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    ENVIRONMENT = None

    def __init__(self):
        environment = ''
        if( len(sys.argv)<=1):
            environment = 'development'
        else:
            environment = sys.argv[1]
        self.config = self.LoadConfig(environment)
    
    def LoadConfig(self, environment):
        if(environment == ''):
            environment = "development"

        ENVIRONMENT = environment

        configFilePath = 'config.'+ENVIRONMENT+'.toml'

        return toml.load(configFilePath)

