import cbpro
import time
from CBFunctions import CBFunctions

realAPI = open('realAPI', 'r').read().splitlines()
sandboxAPI = open('sandBoxAPI', 'r').read().splitlines()

public = sandboxAPI[0]
passphrase = sandboxAPI[1]
secret = sandboxAPI[2]



auth_client = cbpro.AuthenticatedClient(public, secret, passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")

cb = CBFunctions(auth_client)

test = CBFunctions(auth_client)
test.printPrice("BTC-USD")
# Trading Bot Example

sell_price = 53350
sell_amount = 0.1

buy_price = 52852
buy_amount = 0.1




while True:
    price = cb.getPrice("BTC-USD")
    cb.printPrice("BTC-USD")
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
    time.sleep(6)


