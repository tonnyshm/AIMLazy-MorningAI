from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract_abi = [...]  # Add your contract ABI here
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def stake_tokens(amount, wallet_address):
    tx = contract.functions.stakeTokens(amount).build_transaction({
        'from': wallet_address,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(wallet_address)
    })
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)