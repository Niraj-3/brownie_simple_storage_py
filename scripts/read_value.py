from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] #Array of contracts, we get address where it is deployed
    print(simple_storage.retrieve())


def main():
    read_contract()