class CBFunctions:

    def __init__(self, authClient):
        self.authClient = authClient

    def getUser(self):
        print(self.authClient.get_accounts())