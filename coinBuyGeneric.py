import cbpro
from cbpro.authenticated_client import AuthenticatedClient

api_key = ""
api_secret = ""
api_passphrase = ""

class coinBuy:

    client = AuthenticatedClient("","","")

    def __init__(self,key,secret,passphrase) -> cbpro.AuthenticatedClient:
        self.client =  cbpro.AuthenticatedClient(key,secret,passphrase)

    def buy(self, pair, quantity):
        response = self.client.place_market_order(product_id=pair,side='buy',funds=quantity)

    def withdrawCrypto(self,amount,coin,address):
        amount = round(float(amount),8)
        response = self.client.crypto_withdraw(amount,coin,address)
        print("{}: {}".format(coin,response))
    
    def getAvailableBalance(self,coin):

        available = ""

        accounts = self.client.get_accounts()
        for account in accounts:
            currency = account.get('currency',None)
            if currency == coin:
                available = account.get('available',None)
                break

        return available

if __name__ == "__main__":

    RB = coinBuy(api_key,api_secret,api_passphrase)

    #Buy BTC
    RB.buy('BTC-USD',50)
    print("Bought BTC")

    #Buy ETH
    RB.buy('ETH-USD',50)
    print("Bought ETH")

    #Buy LTC
    RB.buy('LTC-USD',50)
    print("Bought LTC")