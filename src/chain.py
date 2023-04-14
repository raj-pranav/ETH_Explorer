# Setup
# from dotenv import get_variables
from web3 import Web3
from decouple import config
import json

API_KEY = config("ALCH_GOERLI_API_KEY")

alchemy_url = f"https://eth-goerli.g.alchemy.com/v2/{API_KEY}"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
# print(w3.is_connected())

# Get the latest block information
latest_block = w3.eth.get_block('latest')
print(f"""
          Block Number   : {latest_block['number']}"
          Block Miner    : {latest_block['miner']}"
          Block Hash     : {latest_block['parentHash'].hex()}"
          Block size     : {latest_block['size']}"
          Block gasUsed  : {latest_block['gasUsed']}
        """ )
# json_string = json.dumps(latest_block)
# print (json_string)
# Get the latest block number
n_1_block = w3.eth.get_block(latest_block['number']-1)
print(f"""
          Block Number   : {n_1_block['number']}"
          Block Miner    : {n_1_block['miner']}"
          Block Hash     : {n_1_block['parentHash'].hex()}"
          Block size     : {n_1_block['size']}"
          Block gasUsed  : {n_1_block['gasUsed']}
        """ )

n_2_block = w3.eth.get_block(latest_block['number']-2)
print(f"""
          Block Number   : {n_2_block['number']}"
          Block Miner    : {n_2_block['miner']}"
          Block Hash     : {n_2_block['parentHash'].hex()}"
          Block size     : {n_2_block['size']}"
          Block gasUsed  : {n_2_block['gasUsed']}
        """ )
# Get the balance of an account
# balance = w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
# print(balance)

# Get the information of a transaction
# tx = w3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
# print(tx)