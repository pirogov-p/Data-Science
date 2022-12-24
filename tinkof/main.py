import pymysql
from connect import host,user,password,db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('CONNECT!')
    print('#' * 20)

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT `id_transaction` FROM `tinkoff.transaction` " \
                      "WHERE `id_transaction` = %s"
                cursor.execute(sql, ('1'))
                result = cursor.fetchone()
                print(result)
    finally:
        connection.close()
except Exception as ex:
    print('EROR')

