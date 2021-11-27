class CBFunctions:

    def __init__(self, authClient):
        self.authClient = authClient

    def sell(self, size, market, productId):
        self.authClient.sell(size=self.size, order_type= self.market, product_id = self.productId)
        print("Sold " + self.productId + " with size of " + self.size + " order type: " + self.market + "at " + self.authClient.get_time())

    def getPrice(self, productID):
        self.price = float(self.authClient.get_product_ticker(product_id='productID')['price'])
        print("ID: "+ self.productID+" PRICE: "+ self.price+" TIME: " + self.authClient.get_time())

    def buy(self, size, market, productID):
        self.authClient.buy(size=self.size, order_type = self.market, product_id= self.productID)
        print("Bought " + self.productID + " with size of " + self.size + "order type: " + self.market + " at " + self.authClient.get_time())