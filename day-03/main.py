from icecream import ic

symbols = []
parts = []

with open("test-input.txt", "r") as file:
	schematic = [[*line.rstrip()] for line in file]

ic(schematic)

symbols_map = {}

for i in range(len(schematic)):
	line = schematic[i]
	for index, item in enumerate(line):
		try:
			is_number = int(item)
		except ValueError:
			if item == ".":
				continue
			else:
				item_coordinates = f"{i}.{index}"
				symbols_map[item_coordinates] = item

ic(symbols_map)