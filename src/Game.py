from Board import *
from Mcts import *
from os import system


def status(player) :
    system(('clear'))
    print("==Tic Tac Toe==")
    if player == 'x' :
        print('--------------\n "x" to move:\n--------------\n' )

    elif player == 'o' :
        print('--------------\n "o" to move:\n--------------\n' )


def and_the_winner_is (winner) :
    system(('clear'))
    print("==Tic Tac Toe==")
    print('-----------------------')
    print(f"{winner} wins!")
    print('-----------------------')

def draw () :
    system(('clear'))
    print("==Tic Tac Toe==")
    print('-----------------------')
    print("It's a draw!")
    print('-----------------------')


def main() :
    GAME_BOARD = Board()
    mcts = MCTS()
    status(GAME_BOARD.player_1)
    print(GAME_BOARD)
    while True :
        coord = int(input())
        coords = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2],}
        coord = coords[coord]
        Result = GAME_BOARD.make_move(coord)
        if Result is not None :
            GAME_BOARD = Board(Result)
            winner = GAME_BOARD.check_winner()
            if winner:
                and_the_winner_is(winner)
                print(GAME_BOARD)
                break

            if not(GAME_BOARD.check_draw()):
                draw()
                print(GAME_BOARD)
                break

            best_move = mcts.search(GAME_BOARD)
            GAME_BOARD = best_move.board
            winner = GAME_BOARD.check_winner()
            if winner:
                and_the_winner_is(winner)
                print(GAME_BOARD)
                break

            if not (GAME_BOARD.check_draw()):
                draw()
                print(GAME_BOARD)
                break
        status(GAME_BOARD.player_1)
        print(GAME_BOARD)


if __name__ == '__main__':
    main()
