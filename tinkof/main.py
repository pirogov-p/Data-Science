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
        with connection.cursor() as cursor:
            insert_list = []
            for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
                insert_list.append(
                    "INSERT INTO tinkoff.transaction (id_transaction, price_peper, peper_count,transaction_type,paper_id)"
                    " VALUES (" + str(i + 5) + ", " + str(i * 108 + 100) + "," + str(10 - i) + ",'buy',1);")
                print(insert_list[i])
                cursor.execute(insert_list[i])
        connection.commit()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM tinkoff.transaction "
            cursor.execute(sql)
            result = cursor.fetchall()
            for a in result:
                print(a)


    finally:
        connection.close()

except Exception as ex:
    print('ERROR')

