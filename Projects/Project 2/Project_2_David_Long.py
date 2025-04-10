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

def BiggestPrime(BigPrime):
    n=0
    start = time.time()
    while time.time() - start < 5: ## current time - time we started calculating less than 3 minutes #Used chatgpt for this
        if is_prime(n):     ## Go through number by number and check for prime, if it is then make it the biggest
            with BigPrime.get_lock():
                BigPrime.value = n
        n += 1
    return BigPrime

def fibonacci(n):
    fibs = []
    a = 0
    b = 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs

def factorial(n):
    facts = 1
    for i in range(1, n+1):
        facts = facts*i
    return facts

def multiprocessor():
    BigPrime = multiprocessing.Value('i', 0)
    processes = [
        multiprocessing.Process(target=BiggestPrime, args=(BigPrime,))
        for _ in range(5)   ## 5 Processes all finding the biggest prime
        ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    return BigPrime.value

def threader():
    thread = threading.Thread(target=BiggestPrime)
    thread.start()
    thread.join()
    return thread

async def asyncrinous():
    return BiggestPrime()

if __name__ == "__main__":
    resultM = multiprocessor()
    fibM = fibonacci(resultM)
    factM = factorial(resultM)
    
    print(f"Multiprocessor Prime: {resultM}")
    print(f"Fibonacci: {fibM}")
    print(f"Factorrial: {factM}")


    ## I ran this and my computer crashed so im giving up for the night lmaooo