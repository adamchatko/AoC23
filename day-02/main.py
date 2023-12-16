from icecream import ic

NO_OF_RED_CUBES = 12
NO_OF_GREEN_CUBES = 13
NO_OF_BLUE_CUBES = 14

sum_of_games_power = 0

with open("input.txt", "r") as file:
	games = [line.rstrip() for line in file]
	for index, game in enumerate(games):
		game_possible = True
		game_id = index + 1
		game_draws = game.split(": ")[1].split("; ")
		max_red_cubes = 0
		max_green_cubes = 0
		max_blue_cubes = 0
		for draw in game_draws:
			draw_colors = draw.split(", ")
			ic(draw_colors)

			for color in draw_colors:
				no_of_cubes = int(color.split(" ")[0])
				if color.endswith("red") and no_of_cubes > max_red_cubes:
					max_red_cubes = no_of_cubes
				if color.endswith("green") and no_of_cubes > max_green_cubes:
					max_green_cubes = no_of_cubes
				if color.endswith("blue") and no_of_cubes > max_blue_cubes:
					max_blue_cubes = no_of_cubes

		game_power = max_red_cubes * max_green_cubes * max_blue_cubes
		sum_of_games_power += game_power

ic(sum_of_games_power)


