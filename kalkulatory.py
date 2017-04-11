print("Halo ziomki !")

def dodawanie(a,b):
	wynik = a+b
	return wynik
	
def get_help():
	print('To jest pomoc')
	
get_help()
a = int(input('Podaj pierwsza liczba'))
b = int(input('Podaj druga liczba'))	

print(dodawanie(a,b))
