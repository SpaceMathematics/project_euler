'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def m_T_or_F():
	x = int(1000 / 3) #How many multiples of 3 are there below 1000
	y = int(999 / 5) #How many multiples of 5 are there below 1000, 999 because 1000 is also divisible by 5
	xy = int(1000 / 15) #How many multiples of 15 are there below 1000, GCD of 3 and 5

	'''
	sum of 3p, where p goes from 1 to value of x
	+ (plus)
	sum of 5q, where q goes from 1 to value of y
	- (minus, since 3 and 5 gave a GCD 15, the multiples are added twice above)
	sum of 15r, where r goes from 1 to value pf xy

	We can pull the constants out of the summation and use the formula n(n + 1)/2 for adding natural nmumbers 1 to n

	Formula : 3x(x + 1)/2 + 5y(y + 1)/2 - 15xy(xy + 1)/2
	'''
	x = x * (x + 1) / 2
	y = y * (y + 1) / 2
	xy = xy * (xy + 1) / 2

	answer = 3 * x + 5 * y - 15 * xy
	print(int(answer))

	'''
	A lot faster than using a loop, O(1) instead of O(n)
	'''

	
m_T_or_F()