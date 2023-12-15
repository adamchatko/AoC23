with open("input.txt", "r") as file:
	lines = [line.rstrip() for line in file]

cal_values_list = []
numbers_as_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
	line_as_list = [*line]
	numbers_dict = {}
	# for item in line_as_list:
	# 	try:
	# 		item_as_int = int(item)
	# 		numbers_dict[item] = line_as_list.index(item)
	# 	except ValueError:
	# 		continue

	for index, value in enumerate(line):
		try:
			item_as_int = int(value)
			number = numbers_as_strings[item_as_int]
			numbers_dict[f"{number}-{index}"] = index
		except ValueError:
			for number in numbers_as_strings:
				substring = line[index:index + len(number)]
				if substring == number:
					numbers_dict[f"{number}-{index}"] = index
					continue

	first_digit_key = min(numbers_dict, key=numbers_dict.get)
	last_digit_key = max(numbers_dict, key=numbers_dict.get)
	first_digit = 0
	last_digit = 0

	for number in numbers_as_strings:
		if first_digit_key.startswith(number):
			first_digit = numbers_as_strings.index(number)
		if last_digit_key.startswith(number):
			last_digit = numbers_as_strings.index(number)

	cal_value = int(f"{first_digit}{last_digit}")
	cal_values_list.append(cal_value)

cal_values_sum = sum(cal_values_list)
print(cal_values_sum)
