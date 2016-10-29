from array import *
my_array = array('i', [1,2,3,4,5])
	
def evenNumbers(num):
	e_sum = 0
	for num in my_array:
		if num%2 == 0:
			temp = num/2
			e_sum = e_sum + temp
			print temp
	print "Total:"		
	print e_sum		

def oddNumbers(num2):
	o_sum = 0
	for num2 in my_array:
		if num2%2 != 0:
			temp2 = num2*2
			o_sum = o_sum + temp2
			print temp2
	print "Total:"
	print o_sum		

print "Even Numbers:"
print(evenNumbers(1))

print "Odd Numbers:"
print(oddNumbers(1))

#print "Sum of Even and Odd Numbers is Array:"
#print e_sum + o_sum				
