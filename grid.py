class TextGrid:
    def __init__(self):
        self.data = []

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
