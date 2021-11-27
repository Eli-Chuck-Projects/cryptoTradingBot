class CBFunctions:

    def __init__(self, authClient):
        self.authClient = authClient

    def getUser(self):
        print(self.authClient.get_accounts())

    def getPrice(self, productID):
        self.price = self.authClient.get_product_ticker(product_id='productID')['price']
        print("ID: "+self.productID+" PRICE: "+self.price+" TIME: "+self.authClient.get_time())