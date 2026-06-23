# Context Manager -- Resource Handler
# __enter__ __exit__ with contextlib @contextmanager
# Real-world App
# DB connections / file I/O
# Overview
# Implements the context manager protocol (__enter__ / __exit__) for safe file handling. __exit__ 
# always closes the file and returns True to suppress exceptions.
#  Also implements the same logic as a @contextmanager generator using contextlib.
#  This is exactly what Python's "with open()" and Django's database transaction.atomic() use internally.
# Problem
# Build FileHandler class and db_connection generator context manager. 
# Both must clean up even if an exception is raised.
# Starter Code
# class FileHandler:
#     def __init__(self, filename, mode): self.file=None; ...
#     def __enter__(self):
#         self.file=open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file: self.file.close()
#         if exc_type: print(f"Error handled: {exc_val}")
#         return True  # suppress exception
# from contextlib import contextmanager
# @contextmanager
# def db_connection(db_name):
#     conn={"db":db_name,"status":"open"}
#     try: yield conn
#     finally: conn["status"]="closed"; print("Connection closed")
# Constraints
# •  __exit__ always runs -- even after exception
# •  Return True from __exit__ to suppress exception
# •  Test with a deliberately raised exception to confirm cleanup
# Bonus:  Build a Timer context manager that prints execution time of any with block.


from contextlib import contextmanager
import time 
class FileHandler:
    def __init__(self, filename, mode):
        self.filename= filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file=open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val):
        print("Closing file...")
        if self.file: 
            self.file.close()

        if exc_type: 
            print(f"Error handled: {exc_val}") 

        return True  # handled the exception dont crash the program 
    

    
print("\n FileHandler Test")

with FileHandler("sample.txt","w") as f:
    f.write("Hello World")
    raise ValueError("File Error")

print("Program Continues...")
    



# f = open("sample.txt", "w")
# f.write("Hello")

# raise ValueError("Error")

# f.close() 

# __enter__()
# ↓
# write
# ↓
# exception
# ↓
# __exit__()
# ↓
# file closed

# to guarantee cleanup even when something fails.