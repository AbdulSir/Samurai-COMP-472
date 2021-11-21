from skeleton import Game
import string

def main():
    g = Game(recommend=True)
    file_name = "gameTrace-" + str(g.gp.size_of_board) + str(len(g.gp.blocs_coordinates)) + str(g.gp.line_up_size) + str(g.gp.threshold) + '.txt'
    print(g.gp.minimax_alphabeta_bool)
    if (g.gp.heuristic_chosen_p1==0):
        heuristic_p1 = " e1(Possible win paths)\n"
    else:
        heuristic_p1 = " e2(Weighted possible win paths)\n"
    if (g.gp.heuristic_chosen_p2==0):
        heuristic_p2 = " e1(Possible win paths)\n\n"
    else:
        heuristic_p2 = " e2(Weighted possible win paths)\n\n"
    with open(file_name , "a") as myfile:
        myfile.write("n=" + str(g.gp.size_of_board) + " b=" + str(len(g.gp.blocs_coordinates)) + " s=" + str(g.gp.line_up_size) +" t=" + str(g.gp.threshold))
        myfile.write("\nblocs= " + str(g.gp.blocs_coordinates) + "\n\n")
        myfile.write("Player 1:" + str(g.gp.play_modes).split('-')[0].upper() + " d=" + str(g.gp.max_depth_d1) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(heuristic_p1)
        myfile.write("Player 2:" + str(g.gp.play_modes).split('-')[1].upper() + " d=" + str(g.gp.max_depth_d2) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(heuristic_p2)

    with open("scoreboard.txt", 'a') as myfile:
        myfile.write("n=" + str(g.gp.size_of_board) + " b=" + str(len(g.gp.blocs_coordinates)) + " s=" + str(g.gp.line_up_size) +" t=" + str(g.gp.threshold))
        myfile.write("\nPlayer 1:" + str(g.gp.play_modes).split('-')[0].upper() + " d=" + str(g.gp.max_depth_d1) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(heuristic_p1)
        myfile.write("Player 2:" + str(g.gp.play_modes).split('-')[1].upper() + " d=" + str(g.gp.max_depth_d2) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(heuristic_p2)
        myfile.write("20 games\n\n")


    g.play()
    print('Number of evaluated states: ' + str(g.nb_of_evaluated_states))
    #g.game_series(10)


if __name__ == "__main__":
    main()