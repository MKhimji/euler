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


def prob5():
    i = 2
    x = 20
    while i < 20:
        if x % i == 0:
            i+=1
        if x % i != 0:
            x+=1
            i=2
        print(x,i)

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
#


