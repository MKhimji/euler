#Find sum of all numbers less than 1000 that are divisible by 3 or 5
#Start with 1, 1 is not divisible by 3 or 5 so move onto 2 etc



#my way

def sum_of_primes():
    i = 0
    my_list=[]
    while i < 1000:
        if i % 3 == 0 or \
           i % 5 == 0:
            my_list.append(i)
        i+=1
    return sum(my_list)


#pythonic way
#range(6) = returns iterable 0,1,2,3,4,5
def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)



#testing with 1000000 shows a performance difference between compute and sum_of_primes.
#compute is faster
