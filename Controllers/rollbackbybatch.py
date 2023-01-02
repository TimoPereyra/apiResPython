from curses import raw
from datetime import timezone, datetime
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


server = 'xxxxxx'
username = 'xxxx' 
password = 'xxxx#x' 
database = 'xxxx'
driver = 'xxxx'



    # Define Variable
ResponseCode=0
Description="Success"
TimeStamp="tiempoAfuturo"
signature = ""
items = []

def rollBackByBatch(request):
    print(request)

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+'')
    # sProcidius = '{call dbo.spAuthenticate_API (@operatorId=?, @token=?)}'
    # with conn.cursor() as cursor:
    #   cursor.execute(sProcidius,params)
    #   data = cursor.fetchall()
    #   print(data[0])

    

    # metodo = "metodoRollBackByBatch"
    # signature = md5Texto(f'{str(metodo)}{(str(idClient))}{str(TimeStamp)}{(str(tokenClient))}')
    print(signature)
    value = {
        "ResponseCode" : ResponseCode,
        "Description": Description,
        "timestamp": TimeStamp,
        "items" : items,
        "signature" : signature}

    return jsonify(value)