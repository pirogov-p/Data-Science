import pymysql

from network import host,user,password,db_name

try:
    connection = pymysql.connect (
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.sursors.DictCursor
    )
except Exception as ex :
    print ('EROR')