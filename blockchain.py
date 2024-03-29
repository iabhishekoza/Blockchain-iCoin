__author__ = "Abhishek Oza"
__version__ = "1.0.0"

# Create the structure of blockchain
# Using Flask == 0.12.2
# Using Postman HTTP Client [test purpose]
# using requests v2.18.4

import datetime
import hashlib
import json
import requests
from uuid import uuid4
from urllib.parse import urlparse
from cryptocurrency import Transactions
import constants

objTrnx = Transactions()


class Blockchain():
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()
        self.node_address = str(uuid4()).replace('-', '')

    def create_block(self, proof, previous_hash):
        trnx = objTrnx.get_trnx()
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': trnx
        }

        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # print('proof_of_work(): ', hash_operation)
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def get_hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        # print('Hash(): ', hashlib.sha256(encoded_block).hexdigest())
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            # 1. Check current and previous block hash
            current_block = self.chain[block_index]
            if current_block['previous_hash'] != self.get_hash(previous_block):
                # print('Hash of current block: ', current_block['previous_hash'], ' and previous_block: ', self.get_hash(previous_block), ' did not match')
                return False

            # 2. Check hash generated are with 4 leading zeros
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                # print('proof_of_work failed: ', hash_operation)
                return False

            previous_block = current_block
            block_index += 1
        return True

    def handle_trnx(self):
        Transactions.add_trnx()
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def create_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_len_chain = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/{constants.get_chain_response()}')
            if response.status_code == 200:
                len_chain = response.json()['number of blocks']
                chain = response.json()['chain']
                if len_chain > max_len_chain and self.is_chain_valid():
                    max_len_chain = len_chain
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
