# Fetch news from multiple sources at the same time using asyncio,
#  so the total time taken is equal to the slowest source, not the sum of all sources.
import asyncio
import time
from pprint import pprint

async def fetch(source: str, delay: float) -> dict:
    await asyncio.sleep(delay)
    return {
        "source": source,
        "headlines": [
            f"{source} story 1",
            f"{source} story 2"
        ]
    }

async def main():
    start = time.time()

    results = await asyncio.gather(
        fetch("BBC", 1.5),
        fetch("Times", 2.0),
        fetch("Reuters", 1.2)
    ) #runs multiple async tasks concurrently and returns all results together in a list

    print("\nNews Feed:\n")
    pprint(results)
    

    print(f"\nDone in {time.time() - start:.1f}s (vs 4.7s sequential)")

asyncio.run(main())