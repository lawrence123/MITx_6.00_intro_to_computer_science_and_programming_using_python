def genPrimes():

    primes = []
    iterator = 1
    
    while True:
        iterator += 1
        for i in primes:
            if iterator % i == 0:
                break
        else:
            primes.append(iterator)
            yield iterator