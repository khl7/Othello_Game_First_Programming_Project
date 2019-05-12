SIZE = 50


class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 3
        self.flips_list = []

    def display(self, check):
        if check == 'True':
            self.color = 0  # Black
            fill(self.color)
            ellipse(self.x, self.y, SIZE, SIZE)
        else:
            self.color = 1  # White
            fill(self.color)
            ellipse(self.x, self.y, SIZE, SIZE)
