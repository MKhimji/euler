#Find sum of all numbers less than 1000 that are divisible by 3 or 5
#Start with 1, 1 is not divisible by 3 or 5 so move onto 2 etc

def prob1():
    i = 0
    my_list=[]
    while i < 1000:
        if i % 3 == 0 or \
           i % 5 == 0:
            my_list.append(i)
        i+=1
    return sum(my_list)

#Returning to prob1 after some time, can I write the above without using list?
#Did it combining two functions
#Can you do it in one?

def prob1_():
    #No point starting at 0 as adding 0 will not affect the sum.
    v = 1
    while v < 1000:
        if v % 3 == 0 or v % 5 == 0:
            yield v
        v+=1
        
def prob1_sum(prob1_):
    a = prob1_()
    return sum(next(a for i in enumerate(a)))

#pythonic way
#range(6) = returns iterable 0,1,2,3,4,5

def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)

#testing with 1000000 shows a performance difference between compute and prob1.
#compute is faster
