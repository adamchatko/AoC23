from icecream import ic

NO_OF_RED_CUBES = 12
NO_OF_GREEN_CUBES = 13
NO_OF_BLUE_CUBES = 14

sum_of_possible_games_ids = 0

with open("input.txt", "r") as file:
	games = [line.rstrip() for line in file]
	for index, game in enumerate(games):
		game_possible = True
		game_id = index + 1
		game_draws = game.split(": ")[1].split("; ")
		for draw in game_draws:
			draw_colors = draw.split(", ")
			for color in draw_colors:
				no_of_cubes = int(color.split(" ")[0])
				if color.endswith("red"):
					if no_of_cubes > NO_OF_RED_CUBES:
						game_possible = False
				if color.endswith("green"):
					if no_of_cubes > NO_OF_GREEN_CUBES:
						game_possible = False
				if color.endswith("blue"):
					if no_of_cubes > NO_OF_BLUE_CUBES:
						game_possible = False
		if game_possible:
			sum_of_possible_games_ids += game_id

ic(sum_of_possible_games_ids)


