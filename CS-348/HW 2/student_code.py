import common
#helpful, but not needed
class variables:
	counter=0


# Counting rule for both functions: count every call to your recursive solver,
# including the first one. A board that arrives already solved returns 1.

def sudoku_backtracking(sudoku):
	def helper(idx):
		variables.counter += 1
		if idx == len(replicables):
			return True
		i, j = replicables[idx]
		for num in range(1, 10):
			if common.can_yx_be_z(sudoku, i, j, num):
				sudoku[i][j] = num
				if helper(idx + 1):
					return True
				sudoku[i][j] = 0
		return False

	variables.counter = 0
	replicables = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				replicables.append((i, j))
	helper(0)
	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	replicables = []
	possible_values = {}
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				replicables.append((i, j))
				for num in range(1, 10):
					if common.can_yx_be_z(sudoku, i, j, num):
						if (i, j) not in possible_values:
							possible_values[(i, j)] = []
						possible_values[(i, j)].append(num)

	def simulate(domains, i, j, num):
		new = {}
		for cell, vals in domains.items():
			if cell == (i, j):
				continue
			ci, cj = cell
			if ci == i or cj == j or (ci // 3 == i // 3 and cj // 3 == j // 3):
				vals = [v for v in vals if v != num]
				if not vals:
					return None
			new[cell] = vals
		return new
	def helper(idx, domains):
		variables.counter += 1
		if idx == len(replicables):
			return True
		i, j = replicables[idx]
		for num in possible_values[(i, j)]:
			if num in domains[(i, j)]:
				sudoku[i][j] = num
				new_domains = simulate(domains, i, j, num)
				if new_domains is not None:
					if helper(idx + 1, new_domains):
						return True
				sudoku[i][j] = 0
			
		return False
	#put your code here

	#initialize the domains for each cell
	#do replicables

	#recursive function to solve the sudoku using forward checking
	#remove numbers from the domains of the cells in the same row, column, and box
	#if any cell has an empty domain, backtrack
	helper(0, possible_values)
	return variables.counter
