
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

UPWARD_TREND_THRESHOLD = .25
DIP_THRESHOLD = -.1

PROFIT_THRESHOLD = .25
STOP_LOSS_THRESHOLD = -.15

lastOpPrice = float(auth_client.get_product_ticker(product_id="BTC-USD")["price"])
print("Starting Price: " + str(lastOpPrice))
buy_amount = 0.1
sell_amount = 0.1


def attemptToMakeTrade():
    currentPrice = float(auth_client.get_product_ticker(product_id="BTC-USD")["price"])
    percentageDiff = (currentPrice - lastOpPrice) / lastOpPrice
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
        lestOpPrice = float(auth_client.get_product_ticker(product_id="BTC-USD")["price"])
        print(auth_client.buy(size=buy_amount,order_type="market", product_id="BTC-USD"))

    isNextOperationBuy = False


def tryToSell(percentageDiff):
    print("Trying to sell")
    print("percent: " + str(percentageDiff))
    global isNextOperationBuy
    global PROFIT_THRESHOLD
    global STOP_LOSS_THRESHOLD

    if percentageDiff >= PROFIT_THRESHOLD:
        print("selling")
        lastOpPrice = float(auth_client.get_product_ticker(product_id="BTC-USD")["price"])
        print(auth_client.sell(size=sell_amount,order_type="market", product_id="BTC-USD"))

    isNextOperationBuy = True

points = []
lastBuyPrice = -1
def attemptToMakeTrade2(dt):
    actionIsBuy = True
    currentPrice = cb.getPrice("BTC-USD")
    points.append(currentPrice)

    if len(points) > 3:
        points.pop(0)
        prev1 = points[1]
        prev2 = points[0]
        s1 = float((currentPrice-prev1)/dt)
        s0 = float((prev1-prev2)/dt)
        if actionIsBuy:
            if s0 < 0 and s1 >= 0:
            #minimum. Buy now
                try:
                    auth_client.buy(size=.1, order_type="market", product_id="BTC-USD")
                    print("BUYING")
                    actionIsBuy = False
                    #This can only happen when an order is verified.
                    lastBuyPrice = currentPrice
                except:
                    print("TRIED to BUY")
        else:
            if s0 > 0 and s1 <= 0 and currentPrice > lastBuyPrice:
            #maximum. Sell now
                try:
                    auth_client.sell(size=.1, order_type="market", product_id="BTC-USD")
                    print("SELLING")
                    actionIsBuy = True
                    #This can only happen when a sale is verified.
                except:
                    print("TRIED to SELL")

    print(points)


while True:
    deltaT = 5
    attemptToMakeTrade2(deltaT)
    time.sleep(deltaT)






