class TextGrid:
    def __init__(self):
        self.data = []
        self.current_x = 0
        self.current_y = 0

    def add_row(self, row):
        self.data.append(row)

    def print(self):
        for y in range(len(self.data)):
            print(self.data[y])

    def rows(self):
        return self.data

    def row_count(self):
        return len(self.data)

    def col_count(self):
        return len(self.data[0])

    def cols(self):
        cols_count = len(self.data[0])
        cols = []
        for x in range(cols_count):
            col = []
            for y in range(len(self.data)):
                col.append(self.data[y][x])
            cols.append(col)

        return cols

    def value_at(self, x, y):
        return self.data[y][x]

    def current_pos(self):
        return (self.current_x, self.current_y)

    def scan_until(self, val):
        while True:

            self.current_x += 1
            if self.current_x >= len(self.data[self.current_y]):
                self.current_y += 1
                self.current_x = 0

            if self.current_y >= len(self.data):
                return False

            if self.data[self.current_y][self.current_x] == val:
                return True

    def take_count_around(self, count):
        start_x, start_y = self.current_pos()
        values = {}
        #left
        left = []
        for i in range(0, count):
            if start_x - i >= 0:
                left.append(self.data[start_y][start_x - i])
        values['left'] = left
        #right 
        right = []
        for i in range(0, count):
            if start_x + i < len(self.data[start_y]):
                right.append(self.data[start_y][start_x + i])
        values['right'] = right
        #down
        down = []
        for i in range(0, count):
            if start_y + i < len(self.data):
                down.append(self.data[start_y + i][start_x])
        values['down'] = down
        up = []
        for i in range(0, count):
            if start_y - i >= 0:
                up.append(self.data[start_y-i][start_x])
        values['up'] = up

        up_left = []
        for i in range(0, count):
            if start_y - i >=0 and start_x - i >= 0:
                up_left.append(self.data[start_y - i][start_x - i])
        values['up_left'] = up_left

        up_right = []
        for i in range(0, count):
            if start_y - i >=0 and start_x + i < len(self.data[start_y]):
                up_right.append(self.data[start_y - i][start_x + i])
        values['up_right'] = up_right

        down_left = []
        for i in range(0, count):
            if start_y + i  < len(self.data) and start_x - i >= 0:
                down_left.append(self.data[start_y + i][start_x - i])
        values['down_left'] = down_left

        down_right = []
        for i in range(0, count):
            if start_y + i < len(self.data) and start_x + i < len(self.data[start_y]):
                down_right.append(self.data[start_y + i][start_x + i])
        values['down_right'] = down_right
        return values

        

            
