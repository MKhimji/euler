import time

# My way
# Use oof as an argument in foo - i.e. sum(foo(oof))
# Or foo as an argument of even_nos - i.e. sum(even_nos(foo))

def oof():
    seq = [1,1]
    for i in seq:
        if seq[-1] + seq[-2] < 4000000:
            seq.append(seq[-2] + seq[-1])
            # if seq[-1] % 2 != 0:
            #     seq.remove(i)
    return seq


def foo(oof):
    before = time.time()

    my_list=[]
    for el in oof():
        my_list.append(el)
        if el % 2 != 0:
            my_list.remove(el)
    after = time.time()
    print("Time Elapsed:", after - before)
    return my_list


# Using even_nos and foo is slower than using oof and foo
def even_nos(foo):
    before = time.time()
    list_of_evens = [2*x for x in range(4000000)]
    after = time.time()

    a = sum(set(foo(oof)).intersection(list_of_evens))
    print("Time Elapsed:", after - before)
    return str(a)
# Some other dudes way

def compute():
        before = time.time()
        ans = 0
        x = 1  # Represents the current Fibonacci number being processed
        y = 2  # Represents the next Fibonacci number in the sequence
        while x <= 4000000:
            if x % 2 == 0:
                ans += x
            x, y = y, x + y

        after = time.time()

        print("Time Elapsed:", after - before)
        return str(ans)


# def fun(n):
#     seq = [1,1]
#     if n == 1:
#         return 1
#     if n == 2:
#         return [1,1]
#     if n >= 3 and n <= 40:
#         seq.append(seq[-2] + seq[-1])
#     return seq

# def test():
#     seq = [1,1]
#     # Need to do a check to make sure the element
#     # appended is less than 4000000

#     seq.append(seq[-2] + seq[-1])


# def foo(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1

# def oof():
#     seq = [1,1]

#     for i in seq:
#         if seq[-1] + seq[-2] < 4000000:
#             seq.append(seq[-2] + seq[-1])
#     return seq







