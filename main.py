from coinbase.wallet.client import Client
import json
client = Client("d6a0fb795e982b6a6b134280e4ba96ae", "eYfwHk3x0bM3GeZlHa7+gciwhtKwMu+LFeu2yxQkxAL0Y4yN7Ls0OmAYKcuWz+hmxTLYyUBpKLORdioPZBID2A==")

user = client.get_current_user();
print(user)
