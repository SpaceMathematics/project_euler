# https://projecteuler.net/problem=1

def total_divisible_by_n(n):
	i = 999 // n
	return ((i * (i + 1)) * n) // 2

print (total_divisible_by_n(3) + total_divisible_by_n(5) - total_divisible_by_n(15))

# RESULT
# 233168
# python3 1/1.2.py  0.02s user 0.02s system 28% cpu 0.141 total