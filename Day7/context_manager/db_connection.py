# import sqlite3

# class DbConnection:
#     def __init__(self,db_name):
#         self.db_name = db_name
#         self.conn = None

#     def __enter__(self):
#         print("Connecting to db...")
#         self.conn = sqlite3.connect(self.db_name)
#         return self.conn
    
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         if exc_type is None:
#             self.conn.commit()
#             print("Transaction committed...")
#         else:
#             self.conn.rollback()
#             print(f"Transaction rolled back... {exc_val}")

#         self.conn.close()
#         print("Connection closed...")

#         return True


from contextlib import contextmanager
import sqlite3

@contextmanager
def database_connection(db_name):
    print("Connecting to database...")
    conn = sqlite3.connect(db_name) #__enter__

    try:
        yield conn # return self.conn 
        #pauses func and give conn to with 
        conn.commit()
        print("Transaction committed")
    except Exception:
        conn.rollback()
        print("Transaction rolled back")
        raise 
    finally:
        conn.close()
        print("Connection closed")


# Create DbConnection object
#         ↓
# __enter__()
#         ↓
# return conn
#         ↓
# Execute with block
#         ↓
# __exit__()
#         ↓
# commit/rollback
#         ↓
# close connection

#generator based 

# Call database_connection()
#         ↓
# Connect database
#         ↓
# yield conn
#         ↓
# Execute with block
#         ↓
# Resume after yield
#         ↓
# commit/rollback
#         ↓
# close connection

