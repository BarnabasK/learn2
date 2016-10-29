#The function isPrime() generates prime numbers.
def isPrime(num):
	p = 2	
	while p <= num:
		for i in range(2, p):
			if p%i == 0:
				p = p + 1
		print "%s" % p
		p = p + 1

print(isPrime(99))				 				