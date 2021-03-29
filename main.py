import robin_stocks.robinhood as r
import pyotp

username = ""
password = ""
My2factorApp = ""

# get user name a password
def getcredentials():
    credentials = open("accountInfo.txt","r")
    username = credentials.readline()
    password = credentials.readline()
    My2factorApp = credentials.readline()
    credentials.close()

# login in using two factor auth
def logintoaccount():
    totp  = pyotp.TOTP(My2factorApp).now()
    login = r.login(username, password, mfa_code=totp)

getcredentials()
logintoaccount()




