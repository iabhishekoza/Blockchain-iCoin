__author__ = "Abhishek Oza"
__version__ = "1.0.0"

from mining import Mining
from cryptocurrency import Transactions
from flask import Flask, jsonify, request, render_template
import constants
import init

# creating web instance
objInit = init.CreateDB()
objMine = Mining()
objTrnx = Transactions()
app = Flask(__name__)

# home page
@app.route('/', methods=['GET'])
def homepage():
    response = {
        1: 'Welcome to Blockchain Demo',
        2: 'Please find below links...',
        3: 'Send money -> localhost:5000/send',
        4: 'Mine a block -> localhost:5000/mine',
        5: 'Fetch all blocks -> localhost:5000/chain',
        6: 'Check if chain is valid -> localhost:5000/checkchain'
    }
    return jsonify(response), 200

# send money
@app.route('/send')
def send_money():
    # return jsonify(objTrnx.add_trnx(node_address, constants.get_miner_name(), constants.get_miner_amount()))
    return render_template("sendmoney.html")


@app.route('/send', methods=['POST'])
def record_trnx():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = request.form['amount']
    objTrnx.add_trnx(sender, receiver, amount)

    response = {
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'Status': 'Success'
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

# all transaction records
@app.route('/utxo', methods=['GET'])
def get_all_transactions():
    return jsonify(objInit.get_all_utxo()), 200

# chains from db
@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify(objInit.get_all_blocks()), 200


# running app
app.debug = True
app.run(host=constants.get_ip_addr(), port=constants.get_port())
