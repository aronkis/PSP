import sqlite3
import json

class Repository():
    def __init__(self, db_path: str = "../database/Hotels.db"):
        self.__connection = sqlite3.connect(db_path)
    
    def GetConnection(self) -> sqlite3.Connection:
        return self.__connection
    
    def SetConnection(self, __connection: sqlite3.Connection) -> None:
        self.__connection = __connection
    
    def OpenConnection(self) -> None:
        self.__connection = sqlite3.connect("../database/Hotels.db")
    
    def CloseConnection(self) -> None:
        if self.__connection:
            self.__connection.close()
            self.__connection = None
        else:
            raise Exception("Connection is already closed.")
    
    def GetData(self, query: str) -> str:
        cursor = self.__connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description]
        cursor.close()
        return json.dumps({"columns": cols, "rows": rows})
    
    def GetDataWithParams(self, query: str, params: list) -> str:
        cursor = self.__connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description]
        cursor.close()
        return json.dumps({"columns": cols, "rows": rows})

    def ModifyData(self, query: str, params: tuple) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(query, params)
        self.__connection.commit()
        cursor.close()
