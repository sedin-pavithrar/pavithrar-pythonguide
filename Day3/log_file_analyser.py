# Log File Analyser 
# Real-world app: DevOps / Server monitoring — AWS / Datadog  
# Problem 
# Build a log file analyser using Python's re module.
#  Given a raw server log string, use regular expressions to extract: all IP addresses, timestamps, HTTP status codes, failed requests (4xx/5xx), email addresses, and replace sensitive data (passwords, tokens) with [REDACTED].

import re

LOG_DATA = """ 

192.168.1.1 - [10/Jun/2026:09:15:01] "GET /api/users" 200 

10.0.0.5    - [10/Jun/2026:09:15:03] "POST /login" 401 

172.16.0.3  - [10/Jun/2026:09:15:07] "GET /dashboard" 200 

192.168.1.1 - [10/Jun/2026:09:15:09] "DELETE /user/5" 500 

Error: admin@company.com password=secret123 token=abc99xyz 

""" 
#returns a list
def extract_ip(log:str) -> list: # log -> str 
    pattern =  r"\d+\.\d+\.\d+\.\d+"
    return re.findall(pattern,log)

def extract_timestamp(log:str) -> list:
    pattern = r"\[(.*?)\]" #(.*?) capture everything inside []
    return re.findall(pattern,log)

def extract_failedcodes(log:str)-> list:
        pattern = r'"([A-Z]+ [^"]+)"\s([45]\d{2})' # GET POST DELETE+URL PATH+STARTS WITH 4 OR 5 + 2DIGITS 
        return re.findall(pattern,log)

def extract_statuscode(log:str)->list:
     pattern = r'"([A-Z]+[^"]+"\s([123]\d{2}))'
     return re.findall(pattern,log)

def extract_email(log:str)-> list:
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    #\b word boundary []->character Set + one or more times \.->to match real dot
    # [one or more letters,digits,._%+-]@[letters,digits,.-].[domain(atleast 2 letter)]
    return re.findall(pattern,log) 

def replace_password(log:str)->list:
     pattern = re.sub(r"password=[^ ]+","password=[REDACTED]",log) # re.sub(pattern,replacement,text)
     return pattern

def replace_tokens(log:str)->list:
     pattern = re.sub(r"token=\S+","token=[REDACTED]",log)
     return pattern



print("IP:")
print(extract_ip(LOG_DATA))

print("Timestamps:")
print(extract_timestamp(LOG_DATA))

print("Error Code:")
print(extract_failedcodes(LOG_DATA))

print("Email:")
print(extract_email(LOG_DATA))

print("HTTP Status Code:")
print(extract_statuscode(LOG_DATA))

print("REDACTED Token:")
print(replace_tokens(LOG_DATA))

print("REDACTED Password:")
print(replace_password(LOG_DATA))


