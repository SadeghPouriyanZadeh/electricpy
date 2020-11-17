# TODO: make function calculate on unknown number of resistances
def equivalent_parallel_resistance(r_1: float, r_2: float) -> float:
	""" Calculate equivalent resistance.

	Args:
		r_1 (float): first resistance
		r_2 (float): second resistance

	Returns:
		float: equivalent resistance
	"""	
	eq_r = (r_1**-1 + r_2**-1)**-1
	return eq_r


# TODO: make function calculate on unknown number of resistances
def equivalent_serial_resistance(r_1: float, r_2: float) -> float:
	""" Calculate serial resistance.

	Args:
		r_1 (float): first resistance
		r_2 (float): second resistance

	Returns:
		float: equivalent resistance
	"""	
	eq_r = r_1 + r_2
	return eq_r


