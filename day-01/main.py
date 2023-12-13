from icecream import ic

with open("input.txt", "r") as file:
	lines = [line.rstrip() for line in file]

cal_values_list = []

for line in lines:
	line_list = [*line]
	new_line_list = []
	for i in range(len(line_list)):
		try:
			new_line_list.append(int(line_list[i]))
		except ValueError:
			continue

	if len(new_line_list) == 1:
		cal_value = int(f"{new_line_list[0]}{new_line_list[0]}")
	else:
		cal_value = int(f"{new_line_list[0]}{new_line_list[-1]}")

	cal_values_list.append(cal_value)

cal_values_sum = sum(cal_values_list)
print(cal_values_sum)