# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>

def total_divisible_by_n(n):
	i = 999 // n
	return ((i * (i + 1)) * n) // 2

print (total_divisible_by_n(3) + total_divisible_by_n(5) - total_divisible_by_n(15))

# RESULT
# 233168
# python3 1/1.2.py  0.02s user 0.02s system 28% cpu 0.141 total