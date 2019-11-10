__author__ = "Abhishek Oza"
__version__ = "1.0.0"

import constants
import pymongo
import json


class CreateDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.db = self.client[constants.get_db()]
        self.trnx_col = self.db[constants.get_trnx_col()]
        self.mined_col = self.db[constants.get_mined_col()]

    def add_trnx_record(self, new_trnx):
        self.trnx_col.insert_one(new_trnx)

    def add_mined_record(self, new_block):
        self.mined_col.insert_one(new_block)

    def get_all_utxo(self):
        response = []
        for record in self.trnx_col.find():
            response.append(record)
        return json.dumps(response, default=str)

    def get_all_blocks(self):
        response = []
        for record in self.mined_col.find():
            response.append(record)
        return json.dumps(response, default=str)