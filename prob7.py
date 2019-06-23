"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number"""

def test():
    n=2
    i=2
    while n<13:
        if n % i == 0:
            n+=1
        if n % i != 0:
            for i in range(n):
                # this doesnt work because there could
                # be other numbers that divide by 0

                pass

def test2():
    mylist2=[]
    for x in range(2, 2, -1):
        mylist2.append(x)
    return mylist2

# prime_gen gives Memory error @ mylist.append(x)

def prime_gen():
    n=2
    mylist=[]
    while n > 1:
        if n % 2 == 0:
            n+=1
        if n % 2 != 0:
            for x in range(n-1, 2, -1):
                if x % 2!= 0:
                    mylist.append(x)
            if all(n % x != 0 for x in mylist):
                yield n
            n+=1

#removed list
#takes ages compared to compute2 
def prime_gen2():
    n=2
    while n > 1:
        if n % 2 == 0:
            n+=1
        a = range(n-1,2,-1)
        if n % 2 != 0:
            if all(n % x != 0 for x in a):
                yield n
        n+=1
        
def prob7(prime_gen2):
    a = prime_gen2()
    return str(next(a for i,a in enumerate(a) if i == 10001))


#compute claims to be quicker than compute2(sieve of eratosthenes)
#atm import error eulerlib prolly coz using different python version, diff libs

# import eulerlib, itertools, sys
# def compute():
# 	ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
# 	return str(ans)


import numpy as np
def compute2():



    import numpy as np

    # We will solve this using the sieve of Eratosthenes
    # The pseudocode can be found at https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

    n = 200000
    sieve = np.array([True for _ in range(n)])
    sieve[0:2] = False
    upper_bound = int(np.sqrt(n))

    for i in range(2, upper_bound+1):
        if sieve[i]:
            j = i * i
            counter = 0
            while j < n:
                sieve[j] = False
                j = (i * i) + (counter * i)
                counter += 1

    primes = np.where(sieve == True)[0]

    # The solution is at index 10000 since we start at index 0
    solution = primes[10000]
    print('solution: ', solution)
