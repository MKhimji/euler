# At the moment i am yielding x as soon as i
# find x that doesnt leave a remainder when divided
# by i. So starting at 20
# 20/2 doesnt leave a remainder
# so i am yielding 20 and then increasing 20
# by 1 to get 21.
def prob():
    # x has to be greater than 20 because
    # when x is < 20 you will always have
    # a decimal number e.g 2/20
    x = 20
    while True:
        alist = [i for i in range(2, 21) if x % i == 0]
        if alist is not None:
            i+=1

        x+=1
        print(x)




def prob6():

    x = 20
    alist = [0 for i in range(2, 21) if x % i == 0]
    return alist


# def prob7():
#     x = 20
#     i = 2

#     while True:
#         i <= 20:
#         if x % i == 0:
#             i+=1
#             x+=1
#     return x


"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def tester():
    i = 2
    x = 10
    while i < 10:
        if x % i == 0:
            i+=1
        if x % i != 0:
            x+=1
            i=2
        print(x,i)
#prob5 - 232792560 - took about 30 seconds  - 1 min
#tester takes 25-30min.

def prob5():
    i = 2
    x = 20
    while i < 20:
        if x % i == 0:
            i+=1
        if x % i != 0:
            x+=1
            i=2
    return(x,i)

def tester2():
    i = 1
    while i < 10:
        print(i)
        i+=1


# x=20 i=2
# x=20 i=3
# x=21 i=2
# x=22 i=2
# x=22 i=3

#############################################################################################

import fractions, math
def compute1():
	ans = 1
	for i in range(1, 21):
		ans *= i // fractions.gcd(i, ans)
	return str(ans)

def compute2():
	ans = 1
	for i in range(1, 21):
		ans *= i // math.gcd(i, ans)
	return str(ans)
# use math instead of fractions

# the following is from github:

# The smallest number n that is evenly divisible by every number in a set {k1, k2, ..., k_m}
# is also known as the lowest common multiple (LCM) of the set of numbers.
# The LCM of two natural numbers x and y is given by LCM(x, y) = x * y / GCD(x, y).
# When LCM is applied to a collection of numbers, it is commutative, associative, and idempotent.
# Hence LCM(k1, k2, ..., k_m) = LCM(...(LCM(LCM(k1, k2), k3)...), k_m).

#eg

#i=1
#1x1//fg(1,1) = 1/1 = 1

#i=2
#1x2//fg(2,1) = 2/1 = 2

#i=3
#2x3/gf(3,2) = 6/1 = 6

# and so on. Final answer depends on ans from the previous loop
# i.e we are getting a value for ans for each iteration.
