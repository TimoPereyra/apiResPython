from lib2to3.pgen2 import token
import pyodbc
from flask import request,jsonify
import hashlib
import os
def md5Texto(texto):
    # Crear un objeto del tipo MD5
    textoMD5 = hashlib.md5()
    # Utilizar el método update para generar el MD5 de la cadena
    textoMD5.update(texto.encode("UTF-8"))
    # Obtener los valores hexadecimales generados del MD5    
    textoMD5 = textoMD5.hexdigest()
    return textoMD5

# from macpath import join
server = 'xxx' 
database = 'xxxx' 
databasetrx = 'xxx' 
username = 'xxxx' 
password = 'xxxx' 

def authenticate(data):

    from datetime import timezone
    import datetime
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)

    # Define Variable
    ResponseCode=0
    Description="Success"
    TimeStamp= int( utc_time.timestamp())
    Token = str(data["token"])
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

    idClient = int(data["partnerid"])
    tokenClient = str(data["token"])

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+'')
    sProcidius = '{call dbo.spAuthenticate_API (@operatorId=?, @token=?)}'
    params = (idClient,tokenClient)
    print(sProcidius,params)
    with conn.cursor() as cursor:
        cursor.execute(sProcidius,params)
        data = cursor.fetchall()
        print(data[0])
        array = []
        for row in data[0]:
            array.append(row)

        ClientId = data[0][1]
        CurrencyId = data[0][4]
        firstName = data[0][6]
        lastName = data[0][7]
        birthDate = data[0][5]

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+databasetrx+';ENCRYPT=yes;UID='+username+';PWD='+password+'')
        sProcidius = '{call dbo.spgAccountBalance (@playerId=?)}'
        params = (idClient)
        print(sProcidius,params)

        with conn.cursor() as cursor:
            cursor.execute(sProcidius,params)
            final = cursor.fetchall()
        
            if (len(final)==0):
                AvaibleBalance= "0"
            else:
                balance = "{:.2f}".format(final[0][0])
                AvaibleBalance = balance
    
    metodo = "metodoGetBalance"
    signature = md5Texto(f'{str(metodo)}{(str(idClient))}{str(TimeStamp)}{(str(tokenClient))}')
    print(signature)
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

    return jsonify(value)