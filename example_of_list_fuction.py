import os 
import sys
os.system('cls')

def creator():
	os.system('cls')
	lista = list()
	while 1:
		try:
			number = int(input('How many names would you like to input?:  '))
			for i in range(number):
				name = input('Name you want to add:  ')
				lista.append(name)
			os.system('cls')
			return lista 
		except:
			print('Intergers Only')
			
def updater(lista):
	os.system('cls')
	print(lista)
	print('\n\n\n')
	print ("""
What would you like to do?
A) Replace a name
B) Append a name
C) Delete a name
D) Exit to main menu
	""")
	
	choice = str(input('Decision:  '))
	while choice.lower() in ('a', 'b', 'c', 'd'):
		if choice.lower() == 'd':
			return lista 
		elif choice.lower() == 'a':
			try:
				number = int(input('Which index would you like to configure?'  ))
				lista[number]
				name = input('What would you like to replace %s with?: '%(lista[number]))
				lista[number] = name
				os.system('cls')
				print(lista)
				return lista
			except:
				print('Index out of range')
				
				
		elif choice.lower() == 'b':
			try:
				number = int(input('How many names would you like to appned?: '))
				for i in range(number):
					name = input('Name you want to add:  ')
					lista.append(name)
				#os.system('cls')
				print(lista)
				return(lista)
			except Exeption as e:
				print(e)
				
def testgrades():
	grades = []
	sun = 0 
	while 1:
		try:
			num = int(input('How many test grades would you like to calculate? :'))
			for i in range(num):
				grade = float(input('Grade?: '))
				grades.append(grade)
			os.system('cls')
			for n in grades:
				sum = sum + n
			ave = sum / len(grades)
			print('Average is :: %s' %(ave))
			return
		except Exception as e:
			print(e)
			
			
def main():
	lista = []
	while 1:
		print("""
What would you like to do?

A) Create a list of names
B) Update a list of names
C) Calculate test grades
Q) Quit
		""")
		
		choice = input('Decision: ')
		while choice.lower() in ('quit', 'q', 'a', 'b', 'c'):
			if choice.lower() in ('quit', 'q'):
				raise SystemExit
				
			elif choice.lower() in ('a'):
				lista = creator()
				choice = str()
				
			elif choice.lower() in ('c'):
				average = testgrades()
				choice = str()
				
			else:
				lista = updater(lista)
				choice = str()
			
if __name__=='__main__':
	main()
				
