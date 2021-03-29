import robin_stocks.robinhood as r
import pyotp

username = ""
password = ""
My2factorApp = ""

# get user name a password
def getCredentials():
    credentials = open("accountInfo.txt","r")
    username = credentials.readline()
    password = credentials.readline()
    My2factorApp = credentials.readline()
    credentials.close()

# login in using two factor auth
def loginToAccount():
    totp  = pyotp.TOTP(My2factorApp).now()
    login = r.login(username, password, mfa_code=totp)

#  get list of owned stocks and writes to file
def getMyStocks():
    my_stocks = r.build_holdings()
    File_object = open("ownedStocks.txt","w")

    # load file with stocks
    for key in my_stocks.keys():
        itemKey = key
        itemValue = my_stocks[itemKey]
        theitem = str(itemKey) + " " + str(itemValue)
        File_object.write(theitem + "\n")
    
    File_object.close()

def buyStock(symbol, quantity):
    r.orders.order_buy_market(symbol, quantity)

def sellStock(symbol, quantity):
    r.orders.order_sell_market(symbol, quantity)

getCredentials()
loginToAccount()
getMyStocks()
# buyStock("BDRBF", 2)
# sellStock("CPRX", 1)

