def discrete_root(start, end, e, y) -> int:
	print("\tSearching in [{:d}, {:d}]".format(start, end))	
		
	if(start > end):
		raise ValueError("Root does not exist")
	
	c = (end + start) // 2 # root candidate
	t = c**e
	print("\tcandidate = {:d}".format(c))
	
	if(t < y):
		return discrete_root(c + 1, end, e, y)
	else:
		if(t > y):
			return discrete_root(start, c - 1, e, y)

	return c

print("Discrete Root Finder")
y = int(input("Insert y = M^e: "))
e = int(input("Insert e: "))
x = discrete_root(0, y, e, y)
print("M = ", x)
