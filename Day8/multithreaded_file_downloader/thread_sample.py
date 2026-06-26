import threading
import time
import random

completed = []
lock = threading.Lock()


def download_file(filename, size_mb):
    delay = random.uniform(1, 4)

    print(f"[START] {filename} on {threading.current_thread().name}")

    time.sleep(delay)  

    # without lock multiple threads try to modify completed list simultaneously
    # lock ensures only one thread accesses the shared resource at a time 

    with lock:
        completed.append(filename) 
        print(f"[DONE]  {filename} in {delay:.1f}s") 


files = [
    ("report.pdf", 5),
    ("video.mp4", 120),
    ("image.jpg", 2),
    ("data.csv", 15)
] 

threads = []

start_time = time.time() 

# Create threads
for file, size in files:
    t = threading.Thread(
        target=download_file,
        args=(file, size)
    )
    threads.append(t)

# Start ALL threads first
for t in threads:
    t.start()

#Then join ALL threads

for t in threads:
    t.join() 

# wait until all thread finishes executing 

end_time = time.time()

print("\nCompleted Files:", completed)

wall_clock = end_time - start_time

# Sequential estimate
sequential_estimate = len(files) * 2.5  # avg delay

print(f"\nWall Clock Time : {wall_clock:.2f} sec")
print(f"Sequential Estimate : {sequential_estimate:.2f} sec")
