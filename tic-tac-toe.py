
gm_placeholder = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def draw_board(nstd_list):
    for x in range(3):
        print(" ---" * 3)
        for y in range(3):
            print("| {} ".format(nstd_list[x][y]), end="")
        print("|")
    print(" ---" * 3)

def p1_move(nstd_list):
    coords = input("Player 1 enter coordinates (x,y): ").split(",")
    x = int(coords[0]) - 1
    y = int(coords[1]) - 1
    nstd_list[x][y] = "X"

def p2_move(nstd_list):
    coords = input("Player 2 enter coordinates (x,y): ").split(",")
    x = int(coords[0]) - 1
    y = int(coords[1]) - 1
    nstd_list[x][y] = "O"

def check_conditions(nstd_list):
    conditions = [
    # check the rows
    len(set(nstd_list[0])) == 1 and nstd_list[0][0] != " ",
    len(set(nstd_list[1])) == 1 and nstd_list[1][0] != " ",
    len(set(nstd_list[2])) == 1 and nstd_list[2][0] != " ",
    # check the columns
    len(set([row[0] for row in nstd_list])) == 1 and nstd_list[0][0] != " ",
    len(set([row[1] for row in nstd_list])) == 1 and nstd_list[0][1] != " ",
    len(set([row[2] for row in nstd_list])) == 1 and nstd_list[0][2] != " ",
    # check diagonals
    len(set([nstd_list[0][2], nstd_list[1][1], nstd_list[2][0]])) == 1 and nstd_list[1][1] != " ",
    len(set([nstd_list[0][0], nstd_list[1][1], nstd_list[2][2]])) == 1 and nstd_list[1][1] != " "
    ]
    return( True in conditions )

def check_empty_space(nstd_list):
    return " " in [elem for row in nstd_list for elem in row]

def game_play(nstd_list):
    draw_board(nstd_list)
    while True:
        if not check_empty_space(nstd_list):
            print("Game drawn.")
            break
        p1_move(nstd_list)
        draw_board(nstd_list)
        if check_conditions(nstd_list):
            print("Player 1 wins.")
            break
        if not check_empty_space(nstd_list):
            print("Game drawn.")
            break
        p2_move(nstd_list)
        draw_board(nstd_list)
        if check_conditions(nstd_list):
            print("Player 2 wins.")
            break

game_play(gm_placeholder)