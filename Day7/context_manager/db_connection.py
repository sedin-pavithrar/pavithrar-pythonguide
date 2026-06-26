import sqlite3

class DbConnection:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        print("Connecting to db...")
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is None:
            self.conn.commit()
            print("Transaction committed...")
        else:
            self.conn.rollback()
            print(f"Transaction rolled back... {exc_val}")

        self.conn.close()
        print("Connection closed...")

        return True
