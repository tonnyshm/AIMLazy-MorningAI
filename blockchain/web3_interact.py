from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

contract_address = os.getenv("TOKEN_CONTRACT_ADDRESS")
abi = [...]  # Your contract ABI

contract = web3.eth.contract(address=contract_address, abi=abi)

def check_staking_rewards(user_address):
    rewards = contract.functions.getStakingRewards(user_address).call()
    return rewards

user_address = "0xYourWalletAddress"
print(f"Your staking rewards: {check_staking_rewards(user_address)} AIMLazy tokens")
