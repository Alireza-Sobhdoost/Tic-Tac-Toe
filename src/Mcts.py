import math
import random


# tree node class definition
class TreeNode():
    # class constructor (create tree node class instance)
    def __init__(self, board, parent):

        self.board = board

        if self.board.check_winner() or not(self.board.check_draw()):
            self.is_terminal = True

        else:
            self.is_terminal = False

        self.is_fully_expanded = self.is_terminal

        self.parent = parent
        self.visits = 0
        self.score = 0
        self.children = {}


class MCTS () :

    def search (self , initial_state, iterates=1000 ):
        self.root = TreeNode(initial_state , None)
        #search for 1000 times
        for iteration in range (iterates) :
            node = self.select(self.root)
            score = self.rollout(node.board)
            self.backpropagate(node,score)

        try :
            return self.get_best_move(self.root, 0)

        except :
            pass

    def select(self , node):
        while not node.is_terminal :
            if node.is_fully_expanded :
                node = self.get_best_move(node , 2)
            else :
                return self.expand(node)

        return node

    def expand (self , node):
        states = node.board.generate_states()
        for state in states :
            if str(state.position) not in node.children :
                new_node = TreeNode(state , node)
                node.children[str(state.position)] = new_node

                if len(states) == len(node.children) :
                    node.is_fully_expanded = True

                return new_node

        print("Shuld not get here !")

    def rollout (self , board) :
        while not board.check_winner() :
            try:
                board = random.choice(board.generate_states())

            except :
                return  0

        # print(board)

        if board.player_2 == 'x' : return  1
        elif board.player_2 == 'o' : return  -1

    def backpropagate (self , node , score) :
        while node is not None :
            node.visits += 1
            node.score += score

            node = node.parent

    def get_best_move(self , node , exlporation_constant):
        best_score = float('-inf')
        best_moves = list()
        for child_node in node.children.values() :
            currant_player = 0
            if child_node.board.player_2 == 'x' : currant_player = 1
            elif child_node.board.player_2 == 'o' : currant_player = -1

            move_score = currant_player * child_node.score / child_node.visits + exlporation_constant * math.sqrt(math.log(node.visits) / child_node.visits)
            # print(f"move score : {move_score}")
            if move_score > best_score :
                best_score = move_score
                best_moves = [child_node]
            elif move_score == best_score :
                best_moves.append(child_node)

        return random.choice(best_moves)