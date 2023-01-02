from curses import raw
from datetime import timezone, datetime
import pyodbc
from flask import request,jsonify
import hashlib
import os
import pymssql  
server = 'xxxxx'
username = 'xxxxx' 
password = 'xxxxx#xxx' 
database = 'xxxxx'
driver = 'xxxxx'
def md5Texto(texto):
    # Crear un objeto del tipo MD5
    textoMD5 = hashlib.md5()
    # Utilizar el método update para generar el MD5 de la cadena
    textoMD5.update(texto.encode("UTF-8"))
    # Obtener los valores hexadecimales generados del MD5    
    textoMD5 = textoMD5.hexdigest()
    return textoMD5

    
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
# Define Variable
# dt = datetime.datetime.now(timezone.utc)
# utc_time = dt.replace(tzinfo=timezone.utc)
items = "Ya va a llegar ese array"
ResponseCode=0
description="Succes"
# TimeStamp= int( utc_time.timestamp())
TimeStamp = "20221022"
transactionId = ""
signature = ""




# # Obtener datos





# # Create Dictionary

res = {
        "operationItems": items,
       "ResponseCode":ResponseCode,
       "description":description,
       "timestamp": TimeStamp,
       "transactionId": transactionId,
       "signature":signature
       
}

def creditBet(request):


    token = request['token']
    playerId = request['OperationItems'][0]['clientId']
    gameId = int(request['GameId'])
    OrderNumber = request['OrderNumber']
    TransactionId = request['TransactionId']
    info = request['Info']
    DeviceTypeId = request['DeviceTypeId']
    TypeId = int(request['TypeId'])
    PossibleWin =float(request['PossibleWin'])
    currencyId = request['currencyid']

    BetCommission= float(request['BetCommission'])
    TrackingId = request['TrackingId']

     # items.append([x for x in request['items']])
    # for i in range(0,len(items)):
    #     print(i)
        


    #FUTURA CONSULTA 
    try:
         conn = pymssql.connect(server, username,password, database)
         
         sProcidius = ("f{}")

         print(sProcidius)
         cursor = conn.cursor() 
         cursor.execute(sProcidius)
         conn.commit()
        #  with conn.cursor() as cursor:
        #      cursor.execute(sProcidius)
         final = cursor.fetchall()
         print(final)
  
            #  if(headerId != None):
            #     for raw in (request['OperationItems']):
            #     #Variables de los items
            #         token = raw['token']
            #         amount = raw['amount']
            #         checkNumber = raw['checkNumber']
            #         winAmount = raw['WinAmount']
            #         cashOutAmount = raw['CashoutAmount']
            #         isWinner = raw['IsWinner']
            #         status = raw['Status']
            #         fillDate = raw['FillDate']
            #         maxWinAmount = raw['MaxWinAmount']
            #         isLive = raw['IsLive']
            #         isCashBack = raw['IsCashBack']
            #         sProcidius = '{call dbo.spiCreditItemSportBook (@bet_id=?, @bet_playerId=?, @bei_token=?, @bei_amount=?, @bei_chechNumber=?, @bei_winAmount=?, @bei_cashoutAmount=?, @bei_isWinner=?, @bei_status=?,@bei_fillDate=?, @bei_maxWinAmount=?, @bei_isLive=?,@bei_isCashBack=?)}'
            #         params1=(headerId,playerId,token,float(amount),int(checkNumber),float(winAmount),float(cashOutAmount),int(isWinner),status,fillDate,float(maxWinAmount),int(isLive),int(isCashBack))
            #         print(sProcidius,params1)

            #         with conn.cursor() as cursor:
            #             cursor.execute(sProcidius,params1)
            #             final = cursor.fetchall()
            #             balanceResDb = "{:.2f}".format(final[0][0])
            #             print(balanceResDb)
    except Exception as e:
       print(e)

    # metodo = "metodoCreditBet"
    # signature = md5Texto(f'{str(metodo)}{(str(playerId))}{str(TimeStamp)}{(str(token))}')
    # print(signature)

    
    return "ok"
    # if(headerId!=None):
    #     resPositiva = {
    #         "operationItems": items,
    #         "ResponseCode":ResponseCode,
    #         "description":description,
    #         "timestamp": request ['timestamp'],
    #         "transactionId": request ['TransactionId'],
    #         "signature": signature

    #     }
    #     return jsonify({"Respuesta":resPositiva})
    # if(headerId==0):
    #     return jsonify({"Respuesta":res})
   

   

    # print(final)
    # 

def saveTxt(request):
   dicc = {}
   dicc = request
   f = open ('request.txt','w')
   f.write(str(dicc))
   f.close()