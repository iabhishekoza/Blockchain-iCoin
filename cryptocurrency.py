__author__ = "Abhishek Oza"
__version__ = "1.0.0"

# create a crypto-currency - iCoin
# Handles list of transactions in database
# Every time a block is mine, 5 pending transactions are passed in each block
# Pending transactions are moved to complete transactions once mined

# using requests v2.18.4
# using mongodb v3.9.0

import requests
from pymongo import MongoClient
from uuid import uuid5
from urllib.parse import urlparse

class TransactionDB:


class Transactions:
