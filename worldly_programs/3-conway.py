# Conway Game
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Creates list of list for the cell.
nextCells = []
for x in range(WIDTH):
	column = [] # Create new column
	for y in range(HEIGHT):
		if random.randomint(0, 1) == 0
			column.append('#')	#Add living cell
		else:
			column.append(' ')	#add dead cell
	nextCells.append(column)	#creating list of column lists

# Main program
while True:
	print('\n\n\n\n\n')	#separate list with new lines
	currentCells = copy.deepcopy(nextCells)

#Print current cells on screen
for y in range(HEIGHT):
	for x in range(WIDTH):
		print(currentCells[x][y], end = ' ')	# Print the living(#) or space(' ')
	print()	 #NEw line at end of row

# Calculate next steps based on current steps of cell.
for x in range(WIDTH):
	for y in range(HEIGHT):
		"""
		Getting neighbouring coordinates
		`%WIDHT` ensures leftCoord is always between ) and Width -1
		"""
		leftCoord = (x - 1) % WIDTH
		rightCoord = (x + 1) % WIDTH
		aboveCoord = (y - 1) % HEIGHT
		belowCoord = (y + 1) % HEIGHT

		#Count number of living neightbors:
		numNeighbors = 0
		if currentCells[leftCoord][aboveCoord] == '#':
			numNeighbors += 1	# Top-left neighbour is alive
		if currentCells[x][aboveCoord] == '#':
			numNeighbours += 1 	# Top-right neighbour is alive
		if currentCells[leftCoord][y] == '#':
			numNeighbours += 1	# Left Neighbour is alive
		if currentCells[rightCoord][y] == '#':
			numNeighbours += 1	# right neighbour is alive
		if currentCells[leftCoord][belowCoord] == '#':
			numNeighbours += 1	# bottom-left neighbour is alive
		if currentCells[x][belowCoord] == '#':
			numNeighbours += 1	# bottom neighbour is alive
		if currentCells [rightCoord][belowCoord] == '#':
			numNeighbours += 1	# Bottom-right neighbour is alive

		#set cell based on Conway Game rules
		if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
			# Living cells with 2 or 3 neighbours stay alive
			nextCells[x][y] = '#'
		elif currentCells[x][y] == ' ' and numNeighbours == 3:
			# dead Cells with 3 neightbours become aliuve
			nextCells[x][y] = '#'
		else:
			# Everything becomes dead or dies
			nextCells[x][y] = ' '
time.sleep(1) # Add a 1-second pause to avoid flickering

