# https://projecteuler.net/problem=2

def fib(n):
	sum = 0
	a = 1
	b = 1
	while b < n:
		if b % 2 == 0:
			sum += b
		a, b = b, a + b
	return sum

print(fib(4000000))

# RESULT
# 4613732
# python3 2/2.1.py  0.02s user 0.02s system 23% cpu 0.173 total