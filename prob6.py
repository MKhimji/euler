"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def prob6():
	sum_of_squares=sum([n**2 for n in range(1, 101)])
	sum_1_101=sum([i for i in range(1, 101)])
	return sum_1_101**2 - sum_of_squares


