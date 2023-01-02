# Define Variable

ResponseCode=0
Description="Success"
TimeStamp=0
Token=""
AvailableBalance=-1
CurrencyId = ""
Signature = ""
Meta=""

# Obtener datos

# Create Dictionary
value = {
       "ResponseCode":ResponseCode,
       "description":Description,
       "timestamp": TimeStamp,
       "token": Token,
       "AvailableBalance":AvailableBalance,
       "currencyId": CurrencyId,
       "signature":Signature,
       "meta": Meta
}


def getResponse():
    return value