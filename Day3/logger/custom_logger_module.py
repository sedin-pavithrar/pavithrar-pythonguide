# Custom Logger Module 
# Real-world app: Any production app — logging system 
# Problem 
# Build your own custom logger module (logger.py) that other Python files can import. 
# The logger must write timestamped log messages to both the terminal and a log file. 
# Support four log levels: INFO, WARNING, ERROR, DEBUG. 
# Each message must include timestamp, level, and message text. 

from datetime import datetime
from pathlib import Path

class Logger:
    LEVELS = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR"
    }

    def __init__(self,log_file = "app.log"):
        logger_dir = Path(__file__).parent
        self.log_file =logger_dir / log_file

    
    def _write(self,level,message):
        if level not in self.LEVELS:
            raise ValueError(f"Invalid log level : {level}")
        timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

        log_entry = f"[{timestamp}] [{level}] {message}"

        print(log_entry)

        with open(self.log_file , "a" , encoding="utf-8") as file:
            file.write(log_entry + "\n") 
              #"a" means append mode
              # Creates the file if it doesn't exist
              # Adds new logs at the end

    def debug(self,message):
            self._write("DEBUG",message)

    def info(self, message):
        self._write("INFO", message)
        
    def warning(self,message):
            self._write("WARNING",message)

    def error(self,message):
            self._write("ERROR",message)

        

# main.py
#    │
#    ├── logger.info(...)
#    │       │
#    │       └── _write("INFO", ...)
#    │               ├── validate level
#    │               ├── create timestamp
#    │               ├── print()
#    │               └── write to file
#    │
#    ├── logger.debug(...)
#    ├── logger.warning(...)
#    └── logger.error(...)