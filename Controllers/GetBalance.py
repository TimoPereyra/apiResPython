from asyncio.windows_events import NULL
from pyexpat import model
from unittest import mock
import pyodbc
import hashlib
import os
#import Models.mGetBalance as  rpGetBalance


from flask import request,jsonify
server = 'serverapuesto.database.windows.net'
username = 'administrador' 
password = 'Admin#2022' 
database = 'apuestotrx'
driver = 'sqlsrv'

def md5Texto(texto):
    # Crear un objeto del tipo MD5
    textoMD5 = hashlib.md5()
    # Utilizar el método update para generar el MD5 de la cadena
    textoMD5.update(texto.encode("UTF-8"))
    # Obtener los valores hexadecimales generados del MD5    
    textoMD5 = textoMD5.hexdigest()
    return textoMD5


def startBalance (idClient, _CurrencyId, _Token):
    from datetime import timezone
    import datetime
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    

    # Define Variable

    ResponseCode=0
    Description="Success"
    TimeStamp=  int(utc_time.timestamp())
    Token=_Token
    AvailableBalance=-1
    CurrencyId = _CurrencyId
    Signature = ""
    Meta=""




   
    idClient = str(idClient)
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+'')
        sProcidius = '{call dbo.spgAccountBalance (@acc_id=?, @playerId=?)}'
        params = (0,idClient)
        print(sProcidius,params)
    except Exception as e:
       print(e)

    with conn.cursor() as cursor:
        cursor.execute(sProcidius,params)
        final = cursor.fetchall()
        print(len(final))
        if (len(final)==0):
            AvailableBalance= "0"
        else:
            balance = "{:.2f}".format(final[0][0])
            AvailableBalance = balance
    
    tokenClient = _Token
    metodo = "metodoGetBalance"
    Signature = md5Texto(f'{str(metodo)}{(str(idClient))}{str(TimeStamp)}{(str(tokenClient))}')
    print(Signature)
    
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
  
   
  
    return "ok"
    
    
def saveTxt():
   f = open ('holamundo.txt','w')
   f.write('hola mundo')
   f.close()
   
    
   
    
    

