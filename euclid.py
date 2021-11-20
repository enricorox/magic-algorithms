def euclid(c, d):
	if d == 0:
		return c
	return euclid(d, c % d)


# iterative Euclid
def it_euclid(c, d):
	while d != 0:
		c, d = d, c % d
	return c
		

if __name__ == "__main__":
	print("Compute the Greatest Common Divider (gcd)")
	a = int(input("Insert a: "))
	b = int(input("Insert b: "))
	print(f"gcd({a},{b}) = {abs(it_euclid(a,b))}")  # gcd is always positive!
