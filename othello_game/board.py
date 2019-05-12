from move import Move

SIZE = 8


class Board:
    '''Class Board'''

    def display(self, width):
        '''Make a 4x4 board'''
        for i in range(width/SIZE, width, width/SIZE):
            strokeWeight(2)
            line(i, 0, i, width)
            line(0, i, width, i)
