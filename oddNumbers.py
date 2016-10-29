#Print odd numbers between 1 and 100
def oddNumbers(num):
	for num in range(1, 100):
		if num%2 != 0:
			print num

print (oddNumbers(25))			