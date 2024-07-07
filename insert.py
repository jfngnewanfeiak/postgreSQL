import psycopg2
import os # 環境変数　MYPASSWORD呼び出し

class INSERT:
    def __init__(self) -> None:
        self.DB_connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.environ.get('MYPASSWORD'),
            database='mytable'
        )
        print('DB connect')
    
    def exec(self) -> None:
        with self.DB_connection:
            with self.DB_connection.cursor() as cursor:
                query = 'select * from mytable;'
                cursor.execute(query=query)
                data = cursor.fetchall()
                print(data)
                data_n = len(data) # databaseの要素数取得
                name = input("type your name")
                food = input ("type your favorite food")
                cursor.execute("insert into mytable (id,name,favorite_food) values(%s,%s,%s)",(data_n,name,food))
            self.DB_connection.commit()
        cursor.close()


if __name__ == "__main__":
    a = INSERT()
    while True:
        a.exec()
        if input("0 or 1") == 1:
            break