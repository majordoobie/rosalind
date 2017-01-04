import os
import sys
from collections import Counter 
import time	
import re, string

os.system('cls')

def counter(dna_string):
	dna_string = list(dna_string)
	dna_counter = Counter(dna_string)
	return dna_counter 
	
	
def main():
	while 1:
		os.system('cls')
		print("""
Would you like to import or enter string?
A) Enter
B) Import 
""")

		choice = input('Decision: ')
		while choice.lower() in ('a', 'b','q'):
			if choice.lower() in ('q'):
				raise SystemExit
			elif choice.lower() in('a'):
				while 1:
					try:
						os.system('cls')
						dna_string = input('Enter your string with no space: ')
						dna_counter = counter(dna_string.upper())
						A = dna_counter['A']
						C = dna_counter['C']
						G = dna_counter['G']
						T = dna_counter['T']
						print('%s %s %s %s' %(A,C,G,T))
						print('\n\n\n\n')
						something = input('Press any key to continue to main menu....')
						choice = str()
					except Exception as e:
						print(e)
						
			else:
				os.system('cls')
				file = open('C:/Users/DoobieJunior/Documents/Programing/Projects/code.txt')
				dna = file.readlines() #read the line as a list
				file.close()
				dna = str(dna) # turns dna list into a string
				dna_string = []
				exterm = re.compile('[\W_]+')
				dna = exterm.sub('', dna)
				dna = dna.strip('n')
				for s in dna:
					dna_string.append(s)
				
				dna_counter = counter(dna_string)	
				A = dna_counter['A']
				C = dna_counter['C']
				G = dna_counter['G']
				T = dna_counter['T']
				print('%s %s %s %s' %(A,C,G,T))
				print('\n\n\n\n')
				something = input('Press any key to continue...')
				break
				
						
if __name__=='__main__':
	main()