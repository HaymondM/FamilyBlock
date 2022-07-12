from dis import Bytecode
from itertools import chain
from solcx import compile_standard, install_solc
from web3 import Web3
from dotenv import load_dotenv
import json

install_solc('0.6.0')


#w3 = Web3(Web3.HTTPProvider(address))
#chainid = 1337
#my_address = "0x671c6c1082EE9dBef67c3482509D4d8eF18a0B46"
# os.getenv("PRIVATE_KEY")
# change this private_key. This is for a local blockchain
#private_key = "0xae2b8ead34c7552317587436ff74200445ccbe2296ec2861e989086e1be87538"
######


# set up blockchain (make vars env vars) Check if connection works for interface


class blockactions:
    def __init__(self, address):

        self.address = address

    def connection(self, address):
        self.w3 = Web3(Web3.HTTPProvider(address))
        isConnected = self.w3.isConnected()
        return isConnected

    def addmaindata(self, my_address, private_key, chainId):
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

        # add these when you need to add your block address and private key
        self.my_address = my_address
        self.private_key = private_key
        self.chainId = chainId
        self.bytecode = complied_sol["contracts"]["FamilyBlock.sol"]["FamilyBlock"]["evm"]["bytecode"]["object"]
        self.abi = json.loads(complied_sol["contracts"]
                              ["FamilyBlock.sol"]["FamilyBlock"]["metadata"]
                              )["output"]["abi"]
        #self.w3 = Web3(Web3.HTTPProvider(self.address))

    def adddata(self, Inna, Inag, Inda, Inba):

        #w3 = Web3(Web3.HTTPProvider(self.my_address))
        # create/build the contract
        FamilyBlock = self.w3.eth.contract(
            abi=self.abi, bytecode=self.bytecode)
        nonce = self.w3.eth.getTransactionCount(self.my_address)
        transaction = FamilyBlock.constructor().buildTransaction(
            {"gasPrice": self.w3.eth.gas_price, "chainId": self.chainId,
                "from": self.my_address, "nonce": nonce}
        )
        # sign
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.private_key)
        # send
        print("Deploying contract...")
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # wait for it to be recived
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Deployed!")
        # get contract address
        familyblock = self.w3.eth.contract(
            address=tx_receipt.contractAddress, abi=self.abi)
        # store the data
        # print(type(Inna))
        ######
        print("Updating contract...")
        store_transaction = familyblock.functions.createFamilyBlockContract().buildTransaction({
            "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId,
            "from": self.my_address, "nonce": nonce + 1
        })
        signed_addperson_txn = self.w3.eth.account.sign_transaction(
            store_transaction, private_key=self.private_key)
        send_addperson_tx = self.w3.eth.send_raw_transaction(
            signed_addperson_txn.rawTransaction)
        # wait for it to be recived
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(
            send_addperson_tx)
        print("Updated!")
        ######
        print("Updating contract...")
        store_transaction = familyblock.functions.addPerson(Inna, Inag, Inda, Inba, nonce).buildTransaction({
            "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId,
            "from": self.my_address, "nonce": nonce + 1
        })
        signed_addperson_txn = self.w3.eth.account.sign_transaction(
            store_transaction, private_key=self.private_key)
        send_addperson_tx = self.w3.eth.send_raw_transaction(
            signed_addperson_txn.rawTransaction)
        # wait for it to be recived
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(
            send_addperson_tx)
        print("Updated!")
        print(familyblock.functions.getTree().call())
