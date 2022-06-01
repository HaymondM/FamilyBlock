from dis import Bytecode
from solcx import compile_standard, install_solc
from web3 import Web3
from dotenv import load_dotenv
import json

install_solc('0.6.0')


with open("./contracts/FamilyBlock.sol", "r") as file:
    familyblock_file = file.read()

complied_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"FamilyBlock.sol": {"content": familyblock_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        }
    },
    solc_version="0.6.0",
)
# BUILD THE JSON FILE/SMART CONTRACT
with open("./build\contracts\FamilyBlock.json", "w") as file:
    json.dump(complied_sol, file)


# get abi
bytecode = complied_sol["contracts"]["FamilyBlock.sol"]["FamilyBlock"]["evm"]["bytecode"]["object"]

abi = json.loads(complied_sol["contracts"]
                 ["FamilyBlock.sol"]["FamilyBlock"]["metadata"]
                 )["output"]["abi"]
######


# set up blockchain (make vars env vars) Check if connection works for interface
def connection(address):
    w3 = Web3(Web3.HTTPProvider(address))
    isConnected = w3.isConnected()
    return isConnected


#w3 = Web3(Web3.HTTPProvider(address))
chainid = 1337
my_address = "0x671c6c1082EE9dBef67c3482509D4d8eF18a0B46"
# os.getenv("PRIVATE_KEY")
# change this private_key. This is for a local blockchain
private_key = "0xae2b8ead34c7552317587436ff74200445ccbe2296ec2861e989086e1be87538"

# FamilyBlock =
