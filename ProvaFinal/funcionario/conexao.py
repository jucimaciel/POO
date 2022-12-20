import pymysql.cursors

def conectar():
    connection = pymysql.connect(
        host='localhost',  
        user='root', 
        password='kladjucireis', 
        database='prova03',    
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor) 
    return connection

