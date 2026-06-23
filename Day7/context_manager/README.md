1. Why Context Managers Exist

Imagine this code:

f = open("sample.txt", "w")
f.write("Hello")

raise ValueError("Error")

f.close()

Problem:

Exception occurs
↓
Program stops
↓
f.close() never executes
↓
Resource leak

Files, database connections, sockets, locks, etc. must always be cleaned up.

Python solves this using:

with something:
    ...

which guarantees cleanup.

2. What Happens Behind the Scenes

When Python sees:

with FileHandler("sample.txt", "w") as f:
    f.write("Hello")

Python internally does something similar to:

obj = FileHandler("sample.txt", "w")

f = obj.__enter__()

try:
    f.write("Hello")
finally:
    obj.__exit__(...)

The with statement automatically calls:

__enter__()

at the beginning and

__exit__()

at the end.

3. Understanding __init__
def __init__(self, filename, mode):
    self.filename = filename
    self.mode = mode
    self.file = None

Purpose:

Store information needed later.

Example:

handler = FileHandler("sample.txt", "w")

After creation:

self.filename = "sample.txt"
self.mode = "w"
self.file = None

Nothing is opened yet.

4. Understanding __enter__
def __enter__(self):
    print("Opening file...")
    self.file = open(self.filename, self.mode)
    return self.file

Runs when entering the with block.

Example:

with FileHandler("sample.txt","w") as f:

Execution:

Create object
↓
Call __enter__()
↓
Open file
↓
Return file object
↓
Store it in variable f

So:

f.write(...)

works because:

f == self.file
5. Understanding __exit__
def __exit__(self, exc_type, exc_val, exc_tb):

Python automatically passes exception details.

Suppose:

raise ValueError("File Error")

Then:

exc_type = ValueError
exc_val  = File Error
exc_tb   = traceback object
Cleanup
if self.file:
    self.file.close()

This is the most important part.

Even if:

raise ValueError(...)

occurs,

__exit__() still executes.

This is the whole purpose of a context manager.

6. Why return True
return True

This tells Python:

"I handled the exception."

Without it:

return False

or no return:

raise ValueError(...)

would crash the program.

With:

return True

output becomes:

Error handled: File Error
Program Continues...

The exception is suppressed.

7. Understanding @contextmanager
from contextlib import contextmanager

This decorator lets us create a context manager without writing:

__enter__()
__exit__()
Traditional Version
class DB:
    def __enter__(self):
        ...
    def __exit__(self):
        ...
Generator Version
@contextmanager
def db_connection():
    ...

Much shorter.

8. Understanding yield

This is the most important concept in your DB example.

try:
    yield conn
finally:
    ...

Execution flow:

with db_connection("StudentDB") as conn:
    print(conn)

Step-by-step:

Step 1

Function starts:

conn = {
    "db": "StudentDB",
    "status": "open"
}
Step 2
yield conn

returns control to the with block.

Now:

conn

inside the with block refers to:

{
    "db": "StudentDB",
    "status": "open"
}
Step 3

After the block finishes:

finally:

runs automatically.

Equivalent to:

__exit__()

in a class-based context manager.

9. Why finally is Important
try:
    yield conn
finally:
    conn["status"] = "closed"

Suppose:

raise RuntimeError("DB Error")

inside the block.

Still:

finally

executes.

Output:

Connection closed

This guarantees cleanup.

10. Exception Propagation Difference

Notice:

FileHandler
return True

suppresses exception.

db_connection
finally:

does not suppress exception.

Therefore:

raise RuntimeError("DB Error")

reaches:

except RuntimeError as e:

and gets caught there.

That's why you see:

Caught DB Error
11. Generator Context Manager Internally

Python converts:

@contextmanager
def db_connection():
    ...

into something conceptually like:

class DBConnection:
    def __enter__(self):
        return conn

    def __exit__(self, *args):
        cleanup()

The decorator builds the class for you.

12. Real-World Examples
File Handling
with open("data.txt") as f:
    data = f.read()
Database
with connection.cursor() as cursor:
    cursor.execute(...)
Thread Locks
with lock:
    shared_resource += 1
Django Transactions
with transaction.atomic():
    save_user()
    save_order()

If anything fails:

Rollback
Cleanup
Exit

automatically.

13. Bug in Your Timer Class

You commented it out, but there is a small bug:

Current
end = time.perf_counter

You forgot parentheses.

You're storing the function itself.

Correct
end = time.perf_counter()

Complete version:

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        print(f"Execution Time: {end - self.start:.2f} sec")
Interview Question

If asked:

"Why use a context manager?"

A strong answer is:

A context manager manages resources safely. It guarantees setup and cleanup using __enter__ and __exit__, even when exceptions occur. Common examples are file handling, database connections, locks, and transactions. It prevents resource leaks and makes code cleaner and safer.

That's the key concept this assignment is teaching.




@contextmanager 
def db_connection(db_name):
    conn={
        "db":db_name,
        "status":"open"
        }
    print(f"Connected to {db_name}")
    try: 
        yield conn
    finally: 
        conn["status"]="closed"
        print("Connection closed")
try:
    with db_connection("StudentDB") as conn:
        print(conn)
        raise RuntimeError("DB Error")
    
except RuntimeError as e:
    print("Caught",e)