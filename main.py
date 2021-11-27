import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

print(public)
print(passphrase)
print(secret)

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

print(auth_client.get_accounts())