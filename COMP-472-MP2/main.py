#from section2 import Game_Parameter
from skeleton import Game
import string

def main():
    g = Game(recommend=True)
    g.play()
    #g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN)
    # gp = Game_Parameter()
    # print(gp.size_of_board)
    # gp.init_board()
    # gp.display_board()
    # gp.coords_of_moves()

if __name__ == "__main__":
    main()