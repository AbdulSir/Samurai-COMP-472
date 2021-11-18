from skeleton import Game
import string

def main():
    g = Game(recommend=True)
    file_name = "gameTrace-" + str(g.gp.size_of_board) + str(len(g.gp.blocs_coordinates)) + str(g.gp.line_up_size) + str(g.gp.threshold) + '.txt'
    with open(file_name , "a") as myfile:
        myfile.write("n=" + str(g.gp.size_of_board) + " b=" + str(len(g.gp.blocs_coordinates)) + " s=" + str(g.gp.line_up_size) +" t=" + str(g.gp.threshold))
        myfile.write("\nblocs= " + str(g.gp.blocs_coordinates) + "\n\n")
        myfile.write("Player 1:" + str(g.gp.play_modes).split('-')[0].upper() + " d=" + str(g.gp.max_depth_d1) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(" e1(Possible win paths)\n")
        myfile.write("Player 2:" + str(g.gp.play_modes).split('-')[1].upper() + " d=" + str(g.gp.max_depth_d2) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
        myfile.write(" e1(Possible win paths)\n\n")

    g.play()
    print('Number of evaluated states: ' + str(g.nb_of_evaluated_states))


if __name__ == "__main__":
    main()