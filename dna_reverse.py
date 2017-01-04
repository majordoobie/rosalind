import os
os.system('cls')

def main():
	file = open('C:/Users/DoobieJunior/Documents/Programing/Projects/thirdcode.txt')
	dna = file.read()        							#Use this to allow string manipulation over readlines()
	file.close()
	dna = dna.strip('\n')
	dna = list(dna)										#Converts the string into a list
	for n,i in enumerate(dna):
		if i == 'T':
			dna[n] = 'A'								#This block of code reads every index and applies
		elif i == 'A':									#an if statement to change the letter to it's
			dna[n] = 'T'								#proper counterpart 
		elif i == 'G':
			dna[n] = 'C'
		else:
			dna[n] = 'G'
	dnar = []
	for i in reversed(dna):								#With all the letters changed to their "partners"
		dnar.append(i)									#we reverse the order and print the string without 
	print(''.join(dnar))								#spaces nor punctuation 
	
if __name__=='__main__':
	main()