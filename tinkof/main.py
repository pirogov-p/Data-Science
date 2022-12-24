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
             my_list = []

             for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
                 my_list.append("INSERT INTO transaction (id_transation, price_paper, peper_count,transaction_type,paper_id)" \
                            " VALUES ("i+5", "i*100", "i",'buy',1);"



             insert_query = "INSERT INTO transaction (id_transation, price_paper, peper_count,transaction_type,paper_id)" \
                            " VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
             cursor.execute(insert_query)
             connection.commit()

        '''with connection.cursor() as cursor:
            sql = "SELECT `id_transaction` FROM `tinkoff.transaction` " \
                 "WHERE `id_transaction` = %s"
            cursor.execute(sql, ('1'))
            result = cursor.fetchone()
            print(result)'''
    finally:
        connection.close()
except Exception as ex:
    print('EROR')

