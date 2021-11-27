import cbpro
import time
from CBFunctions import CBFunctions

sandboxAPI = open('sandBoxAPI', 'r').read().splitlines()

public = sandboxAPI[0]
passphrase = sandboxAPI[1]
secret = sandboxAPI[2]
auth_client = cbpro.AuthenticatedClient(public, secret, passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")
cb = CBFunctions(auth_client)


# Threshold Variables
isNextOperationBuy = True

UPWARD_TREND_THRESHOLD = 1.25
DIP_THRESHOLD = -2.25

PROFIT_THRESHOLD = 1.25
STOP_LOSS_THRESHOLD = -2.00

lastOpPrice = 100.0
buy_amount = 0.1
sell_amount = 0.1

def attemptToMakeTrade():
    currentPrice = cb.getPrice("BTC-USD")
    percentageDiff = (currentPrice - lastOpPrice)/lastOpPrice*100
    if isNextOperationBuy:
        tryToBuy()
    else:
        tryToSell()

def tryToBuy(percentageDiff):
    if percentageDiff >= UPWARD_TREND_THRESHOLD or percentageDiff <= DIP_THRESHOLD:
        lestOpPrice = cb.getPrice("BTC-USD")
        cb.buy(buy_amount, "market", "BTC-USD")
        isNextOperationBuy = False

def tryToSell(percentageDiff):
    if percentageDiff >= PROFIT_THRESHOLD or percentageDiff > STOP_LOSS_THRESHOLD:
        lastOpPrice = cb.getPrice("BTC-USD")
        cb.sell(sell_amount, "market", "BTC-USD")
        isNextOperationBuy = True



