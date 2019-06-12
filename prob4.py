# Long way - look through every pair of 3 digit numbers between 100 and 999
# and append/return/yield results
# Will need to define behaviour of a palindrome number with a class.
# There is probably a tool for this but try to see if you can do it



class Palindrome(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.product = x * y
		self.reverse_int = int(str(self.product)[::-1])

	def prob4(x,y):
		x = 100
		y = 999
		j = 100
		for i in range(100,1000):
			if j * i == 0:
				pass





def prob4(x,y):
	x = 100
	y = 999
	j = 100
	for i in range(100,1000):
		if j * i == 0:
			pass


# def prob4new(x,y):
# 	i = 10000
# 	while True:
# 		if x*y
