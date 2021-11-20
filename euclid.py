def euclid(a,b):
	if b == 0:
		return a
	return euclid(b, a % b)

# iterative Euclid
def it_euclid(a,b):
	while(b != 0):
		a, b = b, a % b
	return a
		

if __name__ == "__main__":
	while(True):
		print("Calcolo il Greatest Common Divider (gcd)")
		a = int(input("Inserisci a: "))
		b = int(input("Inserisci b: "))
		print("gcd("+str(a)+","+str(b)+") =", abs(it_euclid(a,b))) # gcd is always positive!
		print("Premi CTRL+C per uscire...\n")
