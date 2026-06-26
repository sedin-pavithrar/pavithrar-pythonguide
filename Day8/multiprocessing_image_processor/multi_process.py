import multiprocessing
import time


def apply_filter(img):

    # CPU-bound work
    # Threading does not help much here because of Python's GIL.
    # Multiprocessing creates separate processes, each with its own GIL,
    # allowing true parallel execution across CPU cores.

    result = sum(
        i**2
        for i in range(500_000)
    )

    return (
        f"Processed: {img} "
        f"checksum:{result % 9999}"
    )

def main():

    images = [
        f"photo_{i:03d}.jpg"
        for i in range(1, 13)
    ]

    # Single Process
    start = time.time()

    single_results = [
        apply_filter(img)
        for img in images
    ]

    single = time.time() - start

    # Multi Process
    start = time.time()

    with multiprocessing.Pool(
        multiprocessing.cpu_count()
    ) as pool:

        multi_results = pool.map(
            apply_filter,
            images
        )
    multi = time.time() - start

    print("\nSample Results:")
    print("\nSingle Process Samples:")
    for result in single_results[:3]:
        print(result)
    
    print("\nMultiprocessing Samples:")
    for result in multi_results[:3]:
        print(result)
    print()
    
    print(f"Single : {single:.2f} sec")
    print(f"Multi  : {multi:.2f} sec")
    print(f"Speedup: {single/multi:.1f}x")
    
    print(f"CPU core:{multiprocessing.cpu_count()}")



if __name__ == "__main__":
    main()