__author__ = "Abhishek Oza"
__version__ = "1.0.0"

import constants
import pymongo

class CreateDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.dbs = self.client.list_database_names()
        if constants.trnxdb() not in self.dbs:
            self.createTrnxDB()
        if constants.minedBlockdb() not in self.dbs:
            self.createMinedBlockDB()

    def createTrnxDB(self):
        trnxDB = self.client[constants.trnxdb()]

    def createMinedBlockDB(self):
        minedBlockDB = self.client[constants.minedBlockdb()]