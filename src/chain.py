from web3 import Web3, AsyncWeb3

# Using Alchemy provider
API_KEY = "Yl4-IFvmpb4bcfJw2Nzb44mTbIoWMXkb"
HTTPS_ENDPOINT = "https://eth-goerli.g.alchemy.com/v2/Yl4-IFvmpb4bcfJw2Nzb44mTbIoWMXkb"
WEBSOCKET_ENDPOINT = "wss://eth-goerli.g.alchemy.com/v2/Yl4-IFvmpb4bcfJw2Nzb44mTbIoWMXkb"

w3 = Web3(Web3.HTTPProvider(HTTPS_ENDPOINT))

print(w3.is_connected())

latest_block = w3.eth.block_number
print(latest_block)