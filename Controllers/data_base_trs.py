
import pyodbc

driver = 'xxxx'
server = 'xxxxx'
username = 'xxxxxx'
password = 'xxxx#xxx'
database = 'xxxx'
try:
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
