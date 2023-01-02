import json
from pydoc import resolve
from urllib import response


from flask import Flask, render_template,request

from Controllers.Database import conection
#from flask_mysqldb import MySQL
# from flask import request
# from flask import jsonify
#from flask import session 

import json
# import requests
#import urllib.parsed 


app = Flask(__name__)


#**************************************************
#**************************************************
#       SERVER  SQL
#**************************************************
#**************************************************




#LOCAL SERVER



#**************************************************
#**************************************************
#       FUNCIONES       GENERALES
#**************************************************
#**************************************************


@app.route('/', methods=['GET', 'POST'])
def home():
        return render_template('home.html')


#**************************************************
#**************************************************
#               GET USER INFO
#**************************************************
#**************************************************

@app.route('/api/GetUserInfo', methods=['POST'])
@app.route('/api/getuserinfo', methods=['POST'])

def GetUserInfo():
   data = {
        "partnerid": request.json['partnerid'],
        "token": request.json['token'] 
       }
   
   import Controllers.cGetUserInfo as aut
   return aut.authenticate(data)
   
   


#**************************************************
#**************************************************
#               GET BALANCE
#**************************************************
#**************************************************


@app.route('/api/GetBalance', methods=['POST'])
@app.route('/api/getbalance', methods=['POST'])
def GetBalance():
   idClient = request.json['ClientId']
   CurrencyId = request.json['CurrencyId']     
   Token = request.json['Token']     


   import Controllers.GetBalance as gb
   return gb.startBalance(idClient, CurrencyId, Token)
   
        # import Models.mGetBalance as bal
        # return  bal.getResponse()
        #return request.get_json()



#**************************************************
#**************************************************
#               DEBIT BATCH
#**************************************************
#**************************************************


@app.route('/api/DebitBatch', methods=['POST'])
@app.route('/api/debitbatch', methods=['POST'])
def DebitBatch():
        return request.get_json()

#**************************************************
#**************************************************
#               CREDIT BET
#**************************************************
#**************************************************


@app.route('/api/CreditBet', methods=['POST'])
@app.route('/api/creditbet', methods=['POST'])
def CreditBet():
        import Controllers.creditBet as cc

       
        return cc.creditBet(request.json),cc.saveTxt(request.json)



#**************************************************
#**************************************************
#               CHEQUE REDACT
#**************************************************
#**************************************************


@app.route('/api/ChequeRedact', methods=['POST'])
@app.route('/api/chequeredact', methods=['POST'])
def ChequeRedact():
        return request.get_json()


#**************************************************
#**************************************************
#               ROLLBACK BY BATCH
#**************************************************
#**************************************************


@app.route('//apiRollbackByBatch', methods=['POST'])
@app.route('/api/rollbackbybatch', methods=['POST'])
def RollbackByBatch():

        import Controllers.rollbackbybatch as cr

       
        return cr.rollBackByBatch(request.json)
  





if __name__ == '__main__' :
        app.run(debug=True)