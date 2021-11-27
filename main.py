import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

autho_client = cbpro.AuthenticatedClient(public, secret, passphrase)

print(autho_client)