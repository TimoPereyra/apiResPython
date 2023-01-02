import pyodbc 
def conection():
    server = 'xxxxx' 
    database = 'xxxxxx' 
    username = 'xxxxxx' 
    password = 'xxxxxx#x' 

    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
