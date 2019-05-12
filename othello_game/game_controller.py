from stone import Stone
from move import Move
import sys

RANGE = 8
LIMIT = 7
IN_THIRD_PRIORITY_1 = 2
IN_THIRD_PRIORITY_2 = 5


class GameController:
    '''Class GameController'''

    def __init__(self, width, stone):
        '''Constructor for GameController'''
        self.width = width
        self.counter = 0  # Black
        self.stone = stone
        self.moves_list = []
        self.double_move_counter = 0
        self.player_score = 0
        self.score_list = []

    def start_game(self, row, column):
        '''Input row and move to start game'''
        if self.check_valid_move(row, column):
            if self.counter % 2 == 0:
                self.stone.total_row[row][column].display('True')  # Human's
                self.flip_stone(row, column)
                self.counter += 1
                print("AI's turn.")

    def can_go(self):
        '''Check all possible valid moves before making a move.
        If there are no valid moves, go to next player's turn'''
        self.moves_list = []
        if self.counter % 2 == 0:
            current_player = 'player'
            other_player = 'AI'
        else:
            current_player = 'AI'
            other_player = 'Player'

        for i in range(RANGE):
            for j in range(RANGE):
                if self.check_valid_move(i, j):
                    self.moves_list.append([i, j])
        if len(self.moves_list) > 0:
            can_go = True
        else:
            print(
                "No valid move for {}. {}'s turn.".format(
                    current_player, other_player))
            can_go = False
            self.counter += 1  # Go to next player's turn

        return can_go

    def is_edge(self, row, column):
        '''Give row and column, return True if within range'''
        if row == 0 or column == LIMIT or column == 0 or row == LIMIT:
            return True

    def is_corner(self, row, column):
        '''Give row and column, return True if within range'''
        if (
            row == 0 and column == 0) or (
                row == 0 and column == LIMIT) or (
                    row == LIMIT and column == 0) or (
                        row == LIMIT and column == LIMIT):
            return True

    def is_third_away(self, row, column):
        '''Give row and column, return True if within range'''
        if (
            row == IN_THIRD_PRIORITY_1) or (
                column == IN_THIRD_PRIORITY_2) or (
                    column == IN_THIRD_PRIORITY_1) or (
                        row == IN_THIRD_PRIORITY_2):
            return True

    def ai_make_move(self):
        '''Call self.can_go method, if there are valid move, AI makes move.
        If not, check for end game'''
        self.double_move_counter = 0
        priority = ''
        if self.can_go():
            temp_y, temp_x = self.moves_list[0]
            temp = len(self.stone.total_row[temp_y][temp_x].flips_list)
            for row, column in self.moves_list:
                if self.is_corner(row, column):  # 1st priority: corner
                    y = row
                    x = column
                    break
                elif self.is_edge(row, column):  # 2nd priority: edges
                    y = row
                    x = column
                    priority = 'Second'
                    continue
                elif self.is_third_away(row, column):
                    # 3rd priority: 3rd tile from the edges
                    if priority == 'Second':
                        continue
                    else:
                        y = row
                        x = column
                        priority = 'Third'  # Remove 4rd 5th tile priority
                        continue
                else:
                    if priority == 'Second' or priority == 'Third':
                        continue
                    else:
                        if len(
                            self.stone.total_row[row][column].flips_list) >= (
                                temp):
                                # 4th priority: maximum number
                                    # of flippable tiles
                            y = row
                            x = column
                            temp = len(self.stone.total_row[y][x].flips_list)
                        else:
                            continue
                            # If length is not greater than the
                            # current [row, column], we want
                            # it to keep going in the for loop.

            self.stone.total_row[y][x].display('False')
            self.flip_stone(y, x)
            self.counter += 1
            print("Player's turn.")
            if not self.can_go():
                self.double_move_counter += 1
                if not self.can_go():
                    self.double_move_counter += 1
                    # Plus 1 twice because whenever
                    # we call this method. counter is reset to 0
        else:
            self.double_move_counter += 1
            if not self.can_go():
                self.double_move_counter += 1

        if self.double_move_counter == 2:
            print('No more moves for either player. Game ends.')
            self.end_game()

    def check_valid_move(self, row, column):
        '''Given row and column, return boolean of whether
        it is a valid move or not'''
        valid_surrounding = False
        other_color = self.other_color()
        current_color = self.current_color()
        surrounding = [[
            0, 1], [
                1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for y_coord, x_coord in surrounding:
            y = row
            x = column
            y += y_coord
            x += x_coord
            if not self.board_or_not(y, x):
                continue
            else:
                if (
                    self.stone.total_row[row][column].color == 3) and (
                        self.stone.total_row[y][x].color == other_color):
                    while True:
                        x += x_coord
                        y += y_coord
                        if not self.board_or_not(y, x):
                            break
                        elif self.stone.total_row[y][x].color == current_color:
                            valid_surrounding = True
                            while True:
                                x -= x_coord
                                y -= y_coord
                                if y == row and x == column:
                                    break
                                (self.stone.total_row[
                                    row][column].flips_list.append(
                                        self.stone.total_row[y][x]))
                            break
        return valid_surrounding

    def flip_stone(self, row, column):
        '''Given move's row and column, flip tiles'''
        for move in self.stone.total_row[row][column].flips_list:
            if self.counter % 2 == 0:
                move.display('True')
            else:
                move.display('False')

    def current_color(self):
        '''Return current player's color'''
        other_color = self.other_color()
        if other_color == 1:
            current_color = 0
        else:
            current_color = 1
        return current_color

    def board_or_not(self, x, y):
        '''Given x, y coordinate, return True if in in range'''
        if x <= LIMIT and x >= 0 and y <= LIMIT and y >= 0:
            return True

    def other_color(self):
        '''Return the other player's color'''
        if self.counter % 2 == 0:  # Human = black move
            other_color = 1  # Other is white
        else:
            other_color = 0  # AI's move
        return other_color

    def end_game(self):
        '''Print end game statements with score for winner'''
        self.player_score = 0
        white_stone_count = 0
        for row in self.stone.total_row:
            for move in row:
                if move.color == 0:
                    self.player_score += 1
                elif move.color == 1:
                    white_stone_count += 1
        if self.player_score > white_stone_count:
            stone = self.player_score
            winner = 'Player wins with'
        elif white_stone_count > self.player_score:
            stone = white_stone_count
            winner = 'AI wins with'
        else:
            stone = white_stone_count
            winner = 'Tie game. Player: '

        fill(0, 0, 255)
        textSize(20)
        text(
            "Game ends. {} {} stones". format(
                winner, stone), self.width/2 - self.width/3, self.width/2)

    def save_to_txt(self, name):
        '''Give player's name, check if it is highest,
        then save to text file'''
        if self.score_list == []:
            self.score_list.append([name, self.player_score])
        else:
            if self.player_score >= int(self.score_list[0][1]):
                self.score_list.insert(0, [name, self.player_score])
            else:
                self.score_list.append([name, self.player_score])
        with open('scores.txt', 'w') as f:
            for name, score in self.score_list:
                f.write('{} {}\n'.format(name, score))

    def get_player_name(self):
        '''Input to get player's name when game ends and returns it'''
        name = self.input('Enter your name')
        if name:
            print('Hello {}. Score is saved'. format(name))
        else:
            print(name)
        return name

    def read_file(self, file):
        '''Read scores.txt file and append it to a list'''
        with open(file) as f:
            for line in f:
                if line != '' and line != '\n':
                    new_line = line.split(' ')
                    self.score_list.append([new_line[0], int(new_line[1])])

    def input(self, message=''):
        '''Convert from Java'''
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
