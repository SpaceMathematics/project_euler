# https://projecteuler.net/problem=2

# def fib(n):
# 	sum = 0
# 	a = 1
# 	b = 1
# 	c = a + b
# 	while c < n:
# 		sum = sum + c
# 		a = b + c
# 		b = a + c
# 		c = a + b
# 	return sum

# print(fib(4000000))

def fib(n):
	sum = 0
	a = 2
	b = 8
	c = 34
	while c < n:
		sum = sum + c
		a = b
		b = c
		c = 4 * b + a
	return sum

print(fib(4000000))
	

# RESULT
# 4613732
# python3 2/2.1.py  0.02s user 0.02s system 23% cpu 0.173 total