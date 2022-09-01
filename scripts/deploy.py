from brownie import accounts,config, SimpleStorage,network
import os

def deploy_simple_storage():
    # There a 3 ways to access an account in brownie
    account = get_account()
    #Using built in ganache accounts;
    # account=accounts[0];
    # print(account)

    #using encrypted command line
    # account = accounts.load("test-account")
    # print(account)
    
    #environment and brownie config
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # or do this
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage) Gives the address where simple storeage was deployed
    stored_value = simple_storage.retrieve();
    print(stored_value)
    transaction = simple_storage.store(15,{"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve();
    print(updated_value)

def get_account():
    if network.show_active()=="development":
        return accounts[0];
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()