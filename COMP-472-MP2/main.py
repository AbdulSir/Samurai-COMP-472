from section2 import Game_Parameter
from skeleton import Game

def main():
    #g = Game(recommend=True)
    #g.play(algo=Game.ALPHABETA,player_x=Game.AI,player_o=Game.AI)
    #g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN)
    gp = Game_Parameter()
    gp.init_board()
    gp.display_board()
    gp.coords_of_moves()

if __name__ == "__main__":
	main()