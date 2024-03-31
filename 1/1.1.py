# https://projecteuler.net/problem=1

sum = 0
for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
print(sum)

# RESULT
# 233168
# python3 1/1.1.py  0.02s user 0.02s system 24% cpu 0.174 total