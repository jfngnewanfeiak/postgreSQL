import psycopg2
import os # 環境変数　MYPASSWORD呼び出し
# DBに接続
connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password=os.environ.get('MYPASSWORD'),
    database='mytable'
)

with connection:
    with connection.cursor() as cursor:
        sql = 'select * from mytable;'
        cursor.execute(query=sql)
        print(cursor.fetchall())
        print('hogehoge')
    connection.commit()
    
cursor.close()