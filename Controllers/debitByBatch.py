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
server = 'xxxxxx' 
database = 'xxxx' 
databasetrx = 'xxxx' 
username = 'xxxx' 
password = 'xxxx#xxx' 

def debitByBatch():
        # Define Variable
    ResponseCode=0
    Description="Success"
    timeStamp="futuroTime"
    item = []
    signature = ""
    #REQUEST ITEMS
    CurrencyId = ""
    OrderNumber= 0
    TransactionId =0
    BetState =1
    ClientId = 1
    Amount=0
    TransactionTypeId =0
    
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+'')
    # sProcidius = '{call dbo.spAuthenticate_API (@operatorId=?, @token=?)}'
    # params = (idClient,tokenClient)
    # print(sProcidius,params)
    # with conn.cursor() as cursor:
    #     cursor.execute(sProcidius,params)
    #     data = cursor.fetchall()
    #     print(data[0])



    #     metodo = "metodoGetUserInfo"
    # signature = md5Texto(f'{str(metodo)}{(str(idClient))}{str(TimeStamp)}{(str(tokenClient))}')

    value = {
        "ResponseCode" : ResponseCode,
        "Description": Description,
        "timestamp": timeStamp,
        "items": item,
        "ClientId" : ClientId,
        "signature" : signature
    }

    return jsonify(value)