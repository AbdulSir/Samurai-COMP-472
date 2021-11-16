#from section2 import Game_Parameter
from skeleton import Game
import string

def main():
    g = Game(recommend=True)
    # file_name = "gameTrace-<" + str(g.gp.size_of_board) + '><' + str(g.gp.num_of_blocs) + '><' + str(g.gp.line_up_size) + '><' + str(g.gp.threshold) + '>.txt'
    # with open('file.txt', "a") as myfile:
    #     myfile.write("n=" + str(g.gp.size_of_board) + " b=" + str(g.gp.num_of_blocs)+ " s=" + str(g.gp.line_up_size) +" t=" + str(g.gp.threshold))
    #     myfile.write("\nblocs= " + str(g.gp.blocs_coordinates) + "\n")
    #     myfile.write("Player 1:" + str(g.gp.play_modes).split('-')[0].upper() + " d=" + str(g.gp.max_depth_d1) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
    #     myfile.write(" e1(Possible win paths)\n")
    #     myfile.write("Player 2:" + str(g.gp.play_modes).split('-')[1].upper() + " d=" + str(g.gp.max_depth_d2) + ' a=' + str(bool(g.gp.minimax_alphabeta_bool)))
    #     myfile.write(" e1(Possible win paths)\n")

    g.play()
    print('Number of evaluated states: ' + str(g.nb_of_evaluated_states))
    #g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN)
    # gp = Game_Parameter()
    # print(gp.size_of_board)
    # gp.init_board()
    # gp.display_board()
    # gp.coords_of_moves()

if __name__ == "__main__":
    main()