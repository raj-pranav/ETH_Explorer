# Setup
# from dotenv import get_variables
from web3 import Web3
from decouple import  config

API_KEY = config("ALCH_GOERLI_API_KEY")
print (API_KEY)

alchemy_url = f"https://eth-goerli.g.alchemy.com/v2/{API_KEY}"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(w3.is_connected())

# Get the latest block number
latest_block = w3.eth.block_number
print(latest_block)

# Get the balance of an account
# balance = w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
# print(balance)

# Get the information of a transaction
# tx = w3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
# print(tx)