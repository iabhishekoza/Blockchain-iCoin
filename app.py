__author__ = "Abhishek Oza"
__version__ = "1.0.0"

from mining import Mining
from flask import Flask, jsonify
import init

# creating web instance
objInit = init.CreateDB()
objMine = Mining()
app = Flask(__name__)

# home page
@app.route('/', methods=['GET'])
def homepage():
    response = {
        1: 'Welcome to Blockchain Demo',
        2: 'Please find below links...',
        3: 'Mine a block -> localhost:5000/mine',
        4: 'Fetch all blocks -> localhost:5000/chain',
        5: 'Check if chain is valid -> localhost:5000/checkchain'
    }
    return jsonify(response), 200

# mining a block
@app.route('/mine', methods=['GET'])
def mine_block():
    return jsonify(objMine.mine_block()), 200

# display full chain
@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(objMine.get_chain()), 200

# check chain validity
@app.route('/checkchain', methods=['GET'])
def check_chain_valid():
    return jsonify(objMine.check_valid_chain()), 200


# running app
app.run(host='0.0.0.0', port=5000)
