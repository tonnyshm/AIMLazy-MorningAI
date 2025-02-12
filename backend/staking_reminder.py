import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))
contract_address = os.getenv("CONTRACT_ADDRESS")
contract_abi = "[...]"  # Replace with actual ABI
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def check_staking_rewards(user_address):
    rewards = contract.functions.getStakingRewards(user_address).call()
    return rewards