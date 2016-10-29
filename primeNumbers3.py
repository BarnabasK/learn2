#The function isPrime() generates prime numbers.
def isPrime(num):
	if num == 2 or num == 3:
		print num
	for i in range(3, int(num**0.5)+1, 2):
			if num%i == 0:
				print i		

print(isPrime(25))				