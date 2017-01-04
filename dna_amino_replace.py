import os
os.system('cls')
	
	
def main():
		file = open('C:/Users/DoobieJunior/Documents/Programing/Projects/secondcode.txt')
		dna = file.read()
		file.close()
		print(dna)
		dna = dna.strip('\n')
		dna = list(dna)
		for n,i in enumerate(dna):
			if i == 'T':
				dna[n]='U'
		print(''.join(dna))
		
if __name__=='__main__':
	main()