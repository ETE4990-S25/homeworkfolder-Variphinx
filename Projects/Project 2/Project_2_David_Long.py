import multiprocessing
import threading
import asyncio
import time

## I used chatgpt to show me how to do this within 3 minutes using time.time()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def BiggestPrime():
    n=0
    start = time.time()
    while time.time() - start < 180: ## current time - time we started calculating less than 3 minutes #Used chatgpt for this
        if is_prime(n):     ## Go through number by number and check for prime, if it is then make it the biggest
            BigPrime = n
        n += 1
    return BigPrime

def multiprocessor():
    run = multiprocessing.Process(target=BiggestPrime)
    run.start()
    run.join()
    return run

def threader():
    thread = threading.Thread(target=BiggestPrime)
    thread.start()
    thread.join()
    return thread

async def asyncrinous():
    return BiggestPrime()