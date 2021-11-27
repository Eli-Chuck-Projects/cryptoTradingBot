import cbpro
import time
from CBFunctions import CBFunctions

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]


print(public)
print(passphrase)
print(secret)

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)


#


# print(auth_client.buy(price="10.0", size="2.1", order_type="limit", product_id="ETH-USD"))
#
#
# # Trading Bot Example
#
# sell_price = 30000
# sell_amount = 0.3
#
# buy_price = 25000
# buy_amount = 0.2
#
# while True:
#     price = float(auth_client.get_product_ticker(product_id="BTC-USD")["price"])
#     if price <= buy_price:
#         print("Buying BTC")
#         auth_client.buy(size=buy_amount, order_type="marker", product_id="BTC_USD")
#     elif price >= sell_price:
#         print("Selling BTC")
#         auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-USD")
#     else:
#         print("Nothing")
#     time.sleep(10)


