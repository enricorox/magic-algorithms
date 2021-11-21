import sys


def discrete_root_search(start, end, e, y) -> int:
	print("\tSearching in [{:d}, {:d}]".format(start, end))	
		
	if start > end:
		raise ValueError("Root does not exist")
	
	c = (end + start) // 2  # root candidate
	t = c**e
	print("\tcandidate = {:d}".format(c))
	
	if t < y:
		return discrete_root_search(c + 1, end, e, y)
	else:
		if t > y:
			return discrete_root_search(start, c - 1, e, y)
	return c


def discrete_root(ay, ae):
	return discrete_root_search(0, ay, ae, ay)


if __name__ == "__main__":
	print("Discrete Root Finder")
	y = 16
	e = 4
	if len(sys.argv) == 3:
		y = int(sys.argv[1])
		e = int(sys.argv[2])
	else:
		print(f"Usage: {sys.argv[0]} <M^e> <e>\n")
		print("Using default parameters")

	print(f"y = M^e = {y}")
	print(f"e = {e}")
	x = discrete_root(y, e)
	print("M = ", x)
