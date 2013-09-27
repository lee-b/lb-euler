#!/usr/bin/env python2.7

grid_size = 20
line_len = 4

# directions
N = "N"
NE = "NE"
E = "E"
SE = "SE"
S = "S"
SW = "SW"
W = "W"
NW = "NW"

# (x,y) offsets for moving in directions
deltas = {
	N: (0, -1),
	NE: (1,-1),
	E: (0,1),
	SE: (1,1),
	S: (0,1),
	SW: (-1,1),
	W: (-1,0),
	NW: (-1,-1),
}

# load data
tmp_grid = ( l.rstrip("\n").split(" ") for l in open("data.txt", "r").readlines() if l.strip() != "" )
grid = []
for y in tmp_grid:
	grid_line = []
	for x in y:
		grid_line.append( int(x) )
	grid.append(grid_line)

# check data
def cols():
	min = 10000000000
	max = 0
	for l in grid:
		size = len(l)
		if size > max:
			max = size
		if size < min:
			min = size

	if min != max:
		print("GRID IS INCONSISTENT!")

	return min

def rows():
	return len(grid)

assert cols() == grid_size
assert rows() == grid_size


# grid data access
def num_at_pos(x,y):
	assert x > 0 and x < 21
	assert y > 0 and y < 21

	return grid[x-1][y-1]


def get_line(x1, y1, direction):
	line = []
	count = 1
	i, j = x1, y1
	while count <= line_len:
		line.append( num_at_pos(i,j) )
		i += deltas[direction][0]
		j += deltas[direction][1]
		count += 1
	return line

def line_product(x1, y1, direction):
	prod = 1
	l = get_line(x1,y1, direction)
	for i in l:
		prod *= i
	return prod

def normalise_coords(x1,y1,x2,y2):
	if x1 > x2 and y1 > y2:
		xt,yt = x1,y1
		x1,y1 = x2,y2
		x2,y2 = xt,yt

	return x1,y1,x2,y2

def line_combinations():
	combos_tried = set()

	for x1 in range(1, grid_size+1):
		for y1 in range(1, grid_size+1):
			for direction in deltas.keys():
				# Handling line (x1,y1,direction)

				x2 = x1 + deltas[direction][0] * line_len
				y2 = y1 + deltas[direction][1] * line_len

				if x1 < 1 or x2 < 1 or y1 < 1 or y2 < 1 or x1 > 20 or x2 > 20 or y1 > 20 or y2 > 20:
					# Invalid line (x1,y1)-(x2,y2); cull it
					continue

				cx1,cy1,cx2,cy2 = normalise_coords(x1,y1,x2,y2)
				combo = cx1,cy1,cx2,cy2
				if combo in combos_tried:
					# Duplicate line (x1,y1)-(x2,y2); skip it."
					continue
				else:
					combos_tried.add(combo)


				# yield the line start pos, direction, and product
				yield (x1,y1,direction, line_product(x1,y1, direction))

combos = list(line_combinations())

combo_products = [ c[3] for c in combos ]
print max(combo_products)
