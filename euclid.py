import sys


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
	a = 5
	b = 20
	if len(sys.argv) == 3:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	else:
		print(f"Usage: {sys.argv[0]} <a> <b>\n")
		print("Using default parameters")

	print("Compute the Greatest Common Divider (gcd)")
	print(f"gcd({a},{b}) = {abs(it_euclid(a,b))}")  # gcd is always positive!
