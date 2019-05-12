from move import Move

ST_BL = 3
ST_WH = 4
SIZE = 16


class Stone:
    def __init__(self, width):
        '''Constructor for stone class'''
        self.SPACING = width//SIZE

        self.first_row = [Move(self.SPACING * i, width/SIZE) for i in range(
            1, (width//self.SPACING), 2)]
        self.second_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 1)) for i in range(1, (width//self.SPACING), 2)]
        self.third_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 2)) for i in range(1, (width//self.SPACING), 2)]
        self.fourth_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 3)) for i in range(1, (width//self.SPACING), 2)]

        self.fifth_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 4)) for i in range(1, (width//self.SPACING), 2)]
        self.sixth_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 5)) for i in range(1, (width//self.SPACING), 2)]
        self.seventh_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 6)) for i in range(1, (width//self.SPACING), 2)]
        self.eighth_row = [Move(self.SPACING * i, (width/SIZE + (
            width/(SIZE/2)) * 7)) for i in range(1, (width//self.SPACING), 2)]

        self.total_row = []
        self.total_row.append(self.first_row)
        self.total_row.append(self.second_row)
        self.total_row.append(self.third_row)
        self.total_row.append(self.fourth_row)
        self.total_row.append(self.fifth_row)
        self.total_row.append(self.sixth_row)
        self.total_row.append(self.seventh_row)
        self.total_row.append(self.eighth_row)

    def start_stone(self):
        '''Start the first 4 stone'''
        self.total_row[ST_BL][ST_BL].display('True')
        self.total_row[ST_WH][ST_WH].display('True')
        self.total_row[ST_WH][ST_BL].display('False')
        self.total_row[ST_BL][ST_WH].display('False')
