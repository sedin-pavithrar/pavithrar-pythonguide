class FileHandler:
    def __init__(self, filename, mode):
        self.filename= filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file=open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val,exc_tb):
        print("Closing file...")
        if self.file: 
            self.file.close()

        if exc_type: 
            print(f"Error handled: {exc_val}") 

        return True  # handled the exception dont crash the program 
    



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