import random

class minesweeper:
    def __init__(self):
        print("hello world")
        self.final_board = [["E"]*10 for i in range(10)]
        self.final_board = self.master_board(self.final_board)
        self.final_board = self.randomize_board(self.final_board)

    def master_board(self, board):
        board[0][9] = "M"
        board[1][8] = "M"
        board[2][7] = "M"
        board[3][6] = "M"
        board[4][5] = "M"
        board[5][4] = "M"
        board[6][3] = "M"
        board[7][2] = "M"
        board[8][1] = "M"
        board[9][0] = "M"
        return board

    def randomize_board(self, board):
        # using a master board then shuffling it
        temp_board = board
        random.shuffle(temp_board)
        return temp_board
    
    def start_game(self):
        self.display_board(self.final_board)
        is_victory = self.victory_condition(self.final_board)
        while is_victory == 0:
            self.display_board(self.turn())
            is_victory = self.victory_condition(self.final_board)
        if is_victory == 1:
            print("You win")
        else:
            print("You lose")
    
    def display_board(self, board):
        print("current board:")
        for array in board:
            # E and M is not displayed
            temp_array = []
            for item in array:
                if item != "E" and item != "M":
                    temp_array.append(item)
                else:
                    temp_array.append(" ")
            print(temp_array)
        print()
    
    def victory_condition(self, board):
        total_clear = 1
        for i in range(len(board)):
            if 'X' in board[i]:
                return 2
            if 'E' in board[i]:
                total_clear = 0
        return total_clear
    
    def turn(self):
        # get user input
        position_click_str = input("Enter click coordinates (separate by comma): ")
        click_str = position_click_str.split(",")
        click = []
        for i in click_str:
            click.append(int(i.strip()))
        self.final_board = self.update_board(self.final_board, click)
        return self.final_board

    def update_board(self, board, click):
        self.board = board
        if self.board[click[0]][click[1]] == 'M':
            self.board[click[0]][click[1]] = 'X'
        else:
            self.update_tile(click)
        return self.board
    
    def is_bomb(self, position_x, position_y):
        if self.board[position_x][position_y] == 'M':
            return 1
        return 0
    
    def count_bombs(self, position):
        x_max_length = len(self.board)
        y_max_length = len(self.board[position[0]])
        total_bombs = 0
        if position[0] + 1 < x_max_length:
            if position[1] + 1 < y_max_length:
                total_bombs += self.is_bomb(position[0] + 1, position[1] + 1)
                total_bombs += self.is_bomb(position[0], position[1] + 1)
            total_bombs += self.is_bomb(position[0] + 1, position[1])
            if position[1] - 1 > -1:
                total_bombs += self.is_bomb(position[0] + 1, position[1] - 1)
                total_bombs += self.is_bomb(position[0], position[1] - 1)
        else:
            if position[1] + 1 < y_max_length:
                total_bombs += self.is_bomb(position[0], position[1] + 1)
            if position[1] - 1 > -1:
                total_bombs += self.is_bomb(position[0], position[1] - 1)
        if position[0] - 1 > -1:
            if position[1] + 1 < y_max_length:
                total_bombs += self.is_bomb(position[0] - 1, position[1] + 1)
            total_bombs += self.is_bomb(position[0] - 1, position[1])
            if position[1] - 1 > -1:
                total_bombs += self.is_bomb(position[0] - 1, position[1] - 1)
        return total_bombs
    
    def recursively_call_update(self, position):
        x_max_length = len(self.board)
        y_max_length = len(self.board[position[0]])
        if position[0] + 1 < x_max_length:
            if position[1] + 1 < y_max_length:
                self.update_tile([position[0] + 1, position[1] + 1])
                self.update_tile([position[0], position[1] + 1])
            self.update_tile([position[0] + 1, position[1]])
            if position[1] - 1 > -1:
                self.update_tile([position[0] + 1, position[1] - 1])
                self.update_tile([position[0], position[1] - 1])
        else:
            if position[1] + 1 < y_max_length:
                self.update_tile([position[0], position[1] + 1])
            if position[1] - 1 > -1:
                self.update_tile([position[0], position[1] - 1])
        if position[0] - 1 > -1:
            if position[1] + 1 < y_max_length:
                self.update_tile([position[0] - 1, position[1] + 1])
            self.update_tile([position[0] - 1, position[1]])
            if position[1] - 1 > -1:
                self.update_tile([position[0] - 1, position[1] - 1])
    
    def update_tile(self, position):
        if self.board[position[0]][position[1]] == 'E':
            bombs = self.count_bombs(position)
            if bombs > 0:
                self.board[position[0]][position[1]] = str(bombs)
            else:
                self.board[position[0]][position[1]] = 'B'
                self.recursively_call_update(position)

if __name__ == "__main__":
    minesweeper_game = minesweeper()
    minesweeper_game.start_game()