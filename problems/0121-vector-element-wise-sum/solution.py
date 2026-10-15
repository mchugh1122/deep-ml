def vector_sum(a,b):

	if len(a) != len(b):
		return -1
	return [(x+y) for x, y in zip(a,b)]
