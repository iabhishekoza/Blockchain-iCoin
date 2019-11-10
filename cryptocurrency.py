__author__ = "Abhishek Oza"
__version__ = "1.0.0"

# create a crypto-currency - iCoin
# Handles list of transactions in database
# Every time a block is mine, 5 pending transactions are passed in each block
# Pending transactions are moved to complete transactions once mined

# using mongodb v3.9.0

# from pymongo import MongoClient
# from blockchain import Blockchain
from init import CreateDB
import constants

objDB = CreateDB()


class Transactions:
    def __init__(self):
        self.trnx = []

    def add_trnx(self, sender, receiver, amount):
        new_trnx = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.trnx.append(new_trnx)
        # database entry for each trnx
        objDB.add_trnx_record(new_trnx)

    def get_trnx(self):
        # get 5 transactions from list of transactions
        if len(self.trnx) >= 5:
            trnx_first_5 = self.trnx[:constants.limitTrnx()]
            self.trnx = self.trnx[constants.limitTrnx():]
        else:
            trnx_first_5 = self.trnx
            Transactions.trnx = []
        return trnx_first_5
