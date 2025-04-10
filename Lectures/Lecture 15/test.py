import multiprocessing
import time

def large_calculation(num):
    result = 0
    for i in range(1, 10000000):
        result += i * num
    print(f'Large calculation result for {num}: {result}')

if __name__ == "__main__":
    start_time = time.time()

    processes = []
    for i in range(1, 11):
        p = multiprocessing.Process(target=large_calculation, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")