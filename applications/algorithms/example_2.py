"""
Decimal to binary. Given a decimal number returns
its binary representation  
"""

def main(number):

	
	remainders = []
	remainder = number
	result = number
	
	while result != 0 :
		
		remainder = result % 2
		remainders.append(remainder)
		result = result // 2 # force to do integer division
		
	print("Binary representation of: ", number)
	
	for x in reversed(remainders):
		print(x)
	

if __name__ == '__main__':
	main(13)
