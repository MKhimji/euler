"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number"""

# generator would be long? or would it?
# i only know how yield a value
# and then assign it a var
# e.g a = generator object
# then next(a) to iterate through
# valus

# is there another way to use generators

# start simple
# test to return/yield/print
# next prime number

# start with i = 3
# x for x in range() - doesnt work we dont know the range
# how to write in python:
# if the only numbers that divide a number in range(n) are
# 1 and n.

def prob7():
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




def prob8():
    n=2
    mylist=[]
    while n < 13:
        if n % 2 == 0:
            n+=1
        if n % 2 != 0:
            for x in range(n+1, 13):
                if all(x % n != 0 for j in mylist):
                    mylist.append(x)
            return mylist





