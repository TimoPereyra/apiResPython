import json

# Define Variable
ResponseCode=0
Description="Success"
TimeStamp="0"
Token =""
ClientId =0
CurrencyId =""
firstName =""
lastName =""
gender=1   #1 Masculino 0 Femenino
birthDate=""
BetShopId=""
TerritoryId=""
UserTypeId=2    #Bet shop = 7  Internet = 2
AvaibleBalance =-1
IsBot="false"
PercentLimit=""   #optional
GroupId=""        #optional
UserClass=""      #optional
MinBetAmount=""   #optional
MinSingleBetAmount="" #optional
MinExpressBetAmount=""    #optional
signature = ""

# Create Dictionary
value = {
       "ResponseCode" : ResponseCode,
       "Description": Description,
       "timestamp": TimeStamp,
       "token": Token,
       "ClientId" : ClientId,
       "currencyId" : CurrencyId,
       "firstName": firstName,
       "lastName": lastName,
       "gender=1": gender,   #1 Masculino 0 Femenino
       "birthDate": birthDate,
       "BetShopId": BetShopId,
       "TerritoryId":TerritoryId,
       "UserTypeId": UserTypeId,     #Bet shop = 7  Internet = 2
       "AvaibleBalance": AvaibleBalance,
       "IsBot": IsBot,
       "PercentLimit": PercentLimit,
       "GroupId": GroupId,
       "UserClass": UserClass,
       "MinBetAmount": MinBetAmount,
       "MinSingleBetAmount": MinSingleBetAmount,
       "MinExpressBetAmount":MinExpressBetAmount,
       "signature" : signature
}


def getResponse():
    return value