Concurrency
Threading  •  Multiprocessing  •  asyncio  •  GIL
threading multiprocessing asyncio async/await GIL
Day 8  —  Assignment 1 
Multi-threaded File Downloader
threading Thread Lock concurrent.futures 
Real-world App
IDM / Chrome downloads 
Overview
Creates one Thread per file. Each thread sleeps random(1,4) seconds to simulate download latency.
A threading.Lock protects the shared completed list from race conditions.
All threads start first, then all join -- demonstrating true concurrency.
Wall-clock time equals the longest single download, not the sum. 
Foundation for all async I/O in Python.
Problem
Download multiple files concurrently using threads (random sleep simulates network). 
Track progress safely, compare wall-clock time vs sequential.
Starter Code
import threading, time, random
completed=[]; lock=threading.Lock()
def download_file(filename, size_mb):
    delay=random.uniform(1,4)
    print(f"[START] {filename} on {threading.current_thread().name}")
    time.sleep(delay)
    with lock:
        completed.append(filename)
        print(f"[DONE]  {filename} in {delay:.1f}s")
files=[("report.pdf",5),("video.mp4",120),("image.jpg",2),("data.csv",15)]
threads=[threading.Thread(target=download_file,args=(f,s)) for f,s in files]
# Start ALL threads first, then join all

Constraints
•  threading.Lock protects shared list
•  Start ALL threads before joining any
•  Print wall-clock time vs sequential estimate
Bonus:  Rewrite using concurrent.futures.ThreadPoolExecutor(max_workers=3)