# Wallet creation and management

import os
from flowx_sdk.transaction import Transaction


class Wallet:
    
    def __init__(self):
        self.wallet_address = None
        self._balance = 1000
        self.currency_list = [
            "SUI/USDT",
            "SUI/USDC",
            "SUI/DAI",
            "SUI/BUSD",
            "SUI/EUROC",
            "BTC/USDT",
            "BTC/USDC",
            "BTC/DAI",
            "BTC/BUSD",
            "BTC/EUROC",
            "ETH/USDT",
            "ETH/USDC",
            "ETH/DAI",
            "ETH/BUSD",
            "ETH/EUROC",
            "XRP/USDT",
            "XRP/USDC",
            "XRP/DAI",
            "XRP/BUSD",
            "XRP/EUROC",
            ]
        
    @staticmethod
    def generate_wallet_address():
        """Generate a unique twallet address ."""
        return "0x" + os.urandom(32).hex()
    
    def get_wallet_balance(self, currency):
        # fetch balanace of assets base on the stable coin
        return self._balance

    def send_fund(self, transaction: Transaction) -> Transaction:
        if self._balance > ( transaction.amount + transaction.transaction_charge):
            self._balance -=  self._balance + transaction.transaction_charge
            transaction.status = "successful"
            return transaction
        else:
            transaction.status = "unsuccessful"
            return transaction



