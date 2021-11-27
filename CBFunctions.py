class CBFunctions:

    def __init__(self, authClient):
        self.authClient = authClient

    def sell(self, size, market, productID):
        try:
            print(self.authClient.sell(size=size, order_type= market, product_id = productID))
        except:
            print(self.authClient.sell(size=size, order_type=market, product_id=productID))


    def getPrice(self, productID):
        try:
            price = float(self.authClient.get_product_ticker(product_id=productID)["price"])
            return price
        except:
            print(float(self.authClient.get_product_ticker(product_id=productID)["price"]))
            return;


    def printPrice(self, productID):
        price = float(self.authClient.get_product_ticker(product_id=productID)["price"])
        print("ID: "+str(productID)+" PRICE: $"+str(price)+" TIME: "+str(self.authClient.get_time()))

    def buy(self, size, market, productID):
        try:
            print(self.authClient.buy(size=size, order_type = market, product_id= productID))
        except:
            print(self.authClient.buy(size=size, order_type = market, product_id= productID))