import os 
os.system('cls')



def fibonacci(n,k):
	r = 0 #Rabbits place holder for R
	R = 0 #Total Rabbits
	c = 1 #Simple counter
	s = 0 #Offsprings place holder for S
	S = 1 #Offsprings, we start with one pair so we initialize with 1
	while c <= n -1:
		r = R + S
		s = R * k
		R = r
		S = s
		c = c + 1
	total = R + S
	return total
		
def main():
	print("""
		Welcome to Indian Mathematics calculator, wooo!	
""")
	try:	
		n = int(input('How many months or iterations would you like to process?: '))
		k = int(input('How many pairs does an offspring produce?: '))
		total = fibonacci(n,k)
		print(total)
	except Exception as e:
		print(e)
		
if __name__=='__main__':
	main()
	
	