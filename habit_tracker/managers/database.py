import os
from dotenv import load_dotenv 
import psycopg2
load_dotenv()
class DatabaseManager:
    def __init__(self):
        self.connection = None
        try:
            self.connection = self._connect()
        except Exception as e:
            print(f"Ошибка при подключении к БД: {e}")
            raise  # Пробрасываем исключение дальше для обработки на уровне приложения
    def _connect(self):
        connect=psycopg2.connect(
                host=os.getenv('HOST_DB'),
                port=os.getenv('PORT_DB'),
                dbname=os.getenv('DB'),
                user=os.getenv('USER_DB'),
                password=os.getenv('PASSWORD')
        )
    
        print("соеденение установленно")
        return connect
    def query_database(self,query,params=None,flag_result=True):
        cursor=self.connection.cursor()
        cursor.execute(query)
        if flag_result:
            return cursor.fetchall()
        self.connection.commit()
    def close(self):
        self.connection.close()



DB=DatabaseManager()
print(DB.query_database('select * from test1;'))