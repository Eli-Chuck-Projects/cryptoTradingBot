import cbpro
import time
from CBFunctions import CBFunctions

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]



auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

cb = CBFunctions(auth_client)

test = CBFunctions(auth_client)
test.printPrice("BTC-USD")
# Trading Bot Example

sell_price = 30000
sell_amount = 0.3

buy_price = 25000
buy_amount = 0.2


while True:
    price = cb.getPrice("BTC-USD")
    if price <= buy_price:
        print("Buying BTC")
        # auth_client.buy(size=buy_amount, order_type="marker", product_id="BTC_USD")
        cb.buy(buy_amount, "market", "BTC-USD")
    elif price >= sell_price:
        print("Selling BTC")
        # auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-USD")
        cb.sell(sell_amount, "market", "BTC-USD")
    else:
        print("Nothing")
    time.sleep(10)


