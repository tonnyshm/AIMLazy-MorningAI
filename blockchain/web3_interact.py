import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

if not w3.is_connected():
    raise Exception("Failed to connect to Ethereum network")

def check_balance():
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=[])
    balance = contract.functions.checkBalance().call()
    return balance
