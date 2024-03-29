__author__ = "Abhishek Oza"
__version__ = "1.0.0"

from blockchain import Blockchain
from cryptocurrency import Transactions
from init import CreateDB
import json

# create blockchain instance
objChain = Blockchain()
objTrnx = Transactions()
objInit = CreateDB()


class Mining:
    def mine_block(self):
        previous_block = objChain.get_previous_block()
        proof = objChain.proof_of_work(previous_block['proof'])
        previous_hash = objChain.get_hash(previous_block)
        new_block = objChain.create_block(proof, previous_hash)
        # print('New Block Created: ', new_block)

        # block = {
        #     'index': new_block['index'],
        #     'timestamp': new_block['timestamp'],
        #     'proof': new_block['proof'],
        #     'previous_hash': new_block['previous_hash'],
        #     'transactions': new_block['transactions']
        # }
        # database entry
        objInit.add_mined_record(new_block)

        response = {'message': 'Success! Block is mined'}
        response.update(new_block)
        return json.dumps(response, default=str)

    def get_chain(self):
        if len(objChain.chain) <= 0:
            print('No blocks found, chain is empty')
            return 'No blocks found, chain is empty', 200
        else:
            response = {
                'chain': objChain.chain,
                'number of blocks': len(objChain.chain)
            }
        return response

    def check_valid_chain(self):
        if objChain.is_chain_valid():
            return 'Success! Chain is valid'
        return 'Alert! Chain is invalid'
