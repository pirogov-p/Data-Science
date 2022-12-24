import pymysql
from connect import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `transaction`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `transaction`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)