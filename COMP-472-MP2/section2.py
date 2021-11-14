from skeleton import Game

#Variable setup
size_of_board = num_of_blocs = position_of_blocs = line_up_size = max_depth_d1 = max_depth_d2 = threshold = 0
blocs_x_coord = blocs_y_coord = 0
blocs_coordinates = []
minimax_alphabeta_bool = False #default minimax (False) - Alphabeta (True)
play_modes = ""
board = []

def game_parameter():
    print ("Welcome to the Game of Line 'em Up")

    size_of_board = input("\nPlease Enter the size of the board between 3-10:\n")
    size_of_board = int(size_of_board)

    while (size_of_board < 3) or (size_of_board > 10):
        print("Invalid input")
        size_of_board = input("Please Enter the size of the board between 3-10:\n")
        size_of_board = int(size_of_board)

    num_of_blocs = input("\nPlease Enter the number of blocs between 0-" + str(2*size_of_board) + ":\n")
    num_of_blocs = int(num_of_blocs)

    while (num_of_blocs < 0) or (num_of_blocs > (2*size_of_board)):
        print("Invalid input")
        num_of_blocs = input("\nPlease Enter the number of blocs between 0-" + str(2*size_of_board) + ":\n")
        num_of_blocs = int(num_of_blocs)

    print(num_of_blocs)

    for i in range(num_of_blocs):
        blocs_x_coord = input("Please enter the x coordinate of the bloc " + str(i+1) + "\n")
        blocs_x_coord = int(blocs_x_coord)
        while blocs_x_coord < 0 or blocs_x_coord > size_of_board:
            print("Invalid input")
            blocs_x_coord = input("Please enter the x coordinate of the bloc " + str(i+1) + "\n")
            blocs_x_coord = int(blocs_x_coord)

        #Take in Y coordinates
        blocs_y_coord = input("Please enter the y coordinate of the bloc " + str(i+1) + "\n")
        blocs_y_coord = int(blocs_y_coord)
        while blocs_y_coord < 0 or blocs_y_coord > size_of_board:
            print("Invalid input")
            blocs_y_coord = input("Please enter the y coordinate of the bloc " + str(i+1) + "\n")
            blocs_y_coord = int(blocs_y_coord)

        blocs_coordinates.append((blocs_x_coord, blocs_y_coord))

    print (blocs_coordinates)

    line_up_size = input("\nPlease enter the winning line-up size 3-" + str(size_of_board) + ":\n")
    line_up_size = int(line_up_size)

    while (line_up_size < 3) or (line_up_size > size_of_board):
        print("Invalid input")
        line_up_size = input("Please enter the winning line-up size 3-" + str(size_of_board) + ":\n")
        line_up_size = int(line_up_size)

    print(line_up_size)

    threshold = input("\nPlease enter the maximum allowed time (in seconds) for the program to return a move:\n")
    threshold = int(threshold)

    search_algo = input("\nPlease enter the desired search algorithm (minimax OR alphabeta):\n")
    while (search_algo.lower() != "minimax") and (search_algo.lower() != "alphabeta"):
        print("Invalid input")
        search_algo = input("\nPlease enter the desired search algorithm (minimax OR alphabeta):\n")

    if search_algo == 'minimax':
        minimax_alphabeta_bool = False
    else:
        minimax_alphabeta_bool = True

    print (minimax_alphabeta_bool)

    play_modes = input("Please enter the play modes (i.e. H-H, H-AI, AI-H, AI-AI):\n")
    while (play_modes.lower() != "h-h") and (play_modes.lower() != "h-ai") and (play_modes.lower() != "ai-h") and (play_modes.lower() != "ai-ai"):
        print("Invalid input")
        play_modes = input("Please enter the play modes (i.e. H-H, H-AI, AI-H, AI-AI):\n")

    print(play_modes)

def print_board(board_size):
    print() 
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append('-')
        print()
        board.append(row)
    print()
    print(board)