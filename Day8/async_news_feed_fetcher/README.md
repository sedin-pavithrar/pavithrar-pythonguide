Async News Feed Fetcher
asyncio async def await asyncio.gather
Real-world App
Inshorts / Google News
Overview
async def fetch() awaits asyncio.sleep() to simulate network I/O without blocking. 
asyncio.gather() runs all fetches concurrently in a single thread. 
Total elapsed time equals max delay, not sum -- showing true concurrency without multiple threads. 
This is the exact model used by FastAPI and aiohttp to handle thousands of requests per second.
Problem
Fetch from 3 sources concurrently using asyncio.gather().
Total time should equal max delay, not the sum.
Starter Code
import asyncio, time
async def fetch(source: str, delay: float) -> dict:
    await asyncio.sleep(delay)
    return {"source":source,"headlines":[f"{source} story 1",f"{source} story 
2"]}
async def main():
    start=time.time()
    results=await asyncio.gather(
        fetch("BBC",1.5), fetch("Times",2.0), fetch("Reuters",1.2))
    print(f"Done in {time.time()-start:.1f}s  (vs 4.7s sequential)")
asyncio.run(main())

Constraints
•  All functions must be async def
•  asyncio.gather() -- not sequential awaits
•  Total time = max(delays), not sum



asyncio.gather() is a high-level Python utility function used to run multiple awaitable objects (like coroutines or tasks) concurrently and return an ordered list of their results. It acts similarly to JavaScript's Promise.all(), allowing you to execute multiple I/O-bound operations without blocking the thread sequentially