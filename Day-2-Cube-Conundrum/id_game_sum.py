data = open("Day-2-Cube-Conundrum/data.txt")
sum = 0

max_red = 12
max_green = 13
max_blue = 14

bad_game = []
good_game = []


def indices(n, w, start=0):
    index = n.find(w, start)
    if index == -1:
        return []
    return [index] + indices(n, w, index + 1)


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

for idx, game in enumerate(data):
    # game_possible = False
    red = 0
    green = 0
    blue = 0
    pulls = game.strip().split(": ")[1].split("; ")
    print("game", idx + 1, pulls)
    for pull in pulls:
        print("pull: ", pull)
        cubes = pull.split(", ")
        for cube in cubes:
            cube_data = cube.split(" ")
            # print("cube: ", cube_data[0], cube_data[1])
            if cube_data[1] == "red" and int(cube_data[0]) > red:
                red = int(cube_data[0])
            elif cube_data[1] == "green" and int(cube_data[0]) > green:
                green = int(cube_data[0])
            elif cube_data[1] == "blue" and int(cube_data[0]) > blue:
                blue = int(cube_data[0])
        if red <= max_red and green <= max_green and blue <= max_blue:
            game_possible = True
        else:
            game_possible = False
            # break
    sum += red * green * blue
    print(red, green, blue, "power:", red * green * blue)
    # print(game_possible)
    # if game_possible:
    #     sum += idx + 1
    #     good_game.append(idx + 1)
    # else:
    #     bad_game.append(idx + 1)

print("achieved:", sum)
print("bad games:", bad_game)
print("good games:", good_game)


data.close()
