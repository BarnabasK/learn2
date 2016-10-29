#The function generates prime numbers in the range of 2 and 100
import math
def isPrime(num):
	for i in range(2, 100):
		is_prime = True
		for j in range(2, int(math.sqrt(i)+1)):
			if i%j == 0:
				is_prime = False
		if is_prime:
			print i

print(isPrime(25))					
