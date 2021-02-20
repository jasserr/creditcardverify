from luhn import *   
from itertools import *

def convertTuple(tup): #the product function from the itertools library gives us the output in a tuple so we have to convert it
    str =  ''.join(tup) 
    return str

for i in product('0123456789',repeat=6): #this loop goes through every possible combination 
	#print(i)
	str = convertTuple(i)
	number='543210'+str+'1234'
	mulnum=int(number) #we converted it to integer because we need to verify the multiple of 123457 (read challenge)
	if (verify(number)) and (mulnum % 123457==0) : #verify is a function from the luhn library used to verify if the credit card number is valid
		print(number)
		print("ok")
