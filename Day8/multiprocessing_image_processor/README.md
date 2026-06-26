Multiprocessing Image Processor
multiprocessing Pool cpu_count GIL explanation
Real-world App
Adobe / Canva / Snapseed
Overview
Uses multiprocessing.Pool.map() to distribute CPU-bound work across all CPU cores. 
apply_filter() computes sum(i^2 for i in range(500,000)) to simulate real image processing.
Benchmarked against single-process to show speedup.
Code comments explain why the GIL blocks threading for CPU bound work -- the most important Python performance concept.
Problem
CPU-bound processing using multiprocessing.Pool. Compare single vs multi-process time. 
Comment why threading will not help here (GIL).
Starter Code
import multiprocessing, time
def apply_filter(img):
    result=sum(i**2 for i in range(500_000))  # CPU work
    return f"Processed: {img}  checksum:{result%9999}"
images=[f"photo_{i:03d}.jpg" for i in range(1,13)]
# Single process
start=time.time(); [apply_filter(i) for i in images]; single=time.time()-start
# Multi-process Pool
start=time.time()
with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
    pool.map(apply_filter, images); multi=time.time()-start
print(f"Single:{single:.2f}s  Multi:{multi:.2f}s  
Speedup:{single/multi:.1f}x")
Constraints
•  Actual CPU-bound computation -- not time.sleep
•  Print both times and speedup ratio
•  Explain GIL in code comment

