class CBFunctions:

    def __init__(self, authClient):
        self.authClient = authClient

    def sell(self, size, market, productID):
        self.authClient.sell(size=size, order_type= market, product_id = productID)
        print("Sold " + str(productID) + " with size of " + str(size) + " order type: " + str(market) + "at " + str(self.authClient.get_time()))

    def price(self, productID):
        price = float(self.authClient.get_product_ticker(product_id=productID)["price"])
        return price

    def printPrice(self, productID):
        price = float(self.authClient.get_product_ticker(product_id=productID)["price"])
        print("ID: "+str(productID)+" PRICE: $"+str(price)+" TIME: "+str(self.authClient.get_time()))

    def buy(self, size, market, productID):
        self.authClient.buy(size=size, order_type = market, product_id= productID)
        print("Bought " + str(productID) + " with size of " + str(size) + "order type: " + str(market) + " at " + str(self.authClient.get_time()))