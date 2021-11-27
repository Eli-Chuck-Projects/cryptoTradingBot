
# test = CBFunctions(auth_client)
# test.printPrice("BTC-USD")
# # Trading Bot Example
#
# sell_price = 53350
# sell_amount = 0.1
#
# buy_price = 52852
# buy_amount = 0.1
#



# while True:
#     price = cb.getPrice("BTC-USD")
#     cb.printPrice("BTC-USD")
#     if price <= buy_price:
#         print("Buying BTC")
#         # auth_client.buy(size=buy_amount, order_type="marker", product_id="BTC_USD")
#         cb.buy(buy_amount, "market", "BTC-USD")
#     elif price >= sell_price:
#         print("Selling BTC")
#         # auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-USD")
#         cb.sell(sell_amount, "market", "BTC-USD")
#     else:
#         print("Nothing")
#     time.sleep(6)
#
#

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

UPWARD_TREND_THRESHOLD = .4
DIP_THRESHOLD = -.3

PROFIT_THRESHOLD = 4
STOP_LOSS_THRESHOLD = -.2

lastOpPrice = cb.getPrice("BTC-USD")
print("Starting Price: " + str(lastOpPrice))
buy_amount = 0.1
sell_amount = 0.1


def attemptToMakeTrade():
    currentPrice = cb.getPrice("BTC-USD")
    percentageDiff = (currentPrice - lastOpPrice) / lastOpPrice * 100
    global isNextOperationBuy
    print(isNextOperationBuy)

    if isNextOperationBuy:
        tryToBuy(percentageDiff)
    else:
        tryToSell(percentageDiff)


def tryToBuy(percentageDiff):
    print("Trying to buy")
    print("percent: " + str(percentageDiff))
    global isNextOperationBuy
    global UPWARD_TREND_THRESHOLD
    global  DIP_THRESHOLD
    if percentageDiff >= UPWARD_TREND_THRESHOLD or percentageDiff <= DIP_THRESHOLD:
        print("buying")
        lestOpPrice = cb.getPrice("BTC-USD")
        cb.buy(buy_amount, "market", "BTC-USD")

    isNextOperationBuy = False


def tryToSell(percentageDiff):
    print("Trying to sell")
    print("percent: " + str(percentageDiff))
    global isNextOperationBuy
    global PROFIT_THRESHOLD
    global STOP_LOSS_THRESHOLD

    if percentageDiff >= PROFIT_THRESHOLD:
        print("selling")
        lastOpPrice = cb.getPrice("BTC-USD")
        cb.sell(sell_amount, "market", "BTC-USD")

    isNextOperationBuy = True

while True:
    attemptToMakeTrade()
    time.sleep(6)




