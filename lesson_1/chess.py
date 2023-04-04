class Figure:
    color = "white"
    place_board = (1, 1)
    move = (1, 1)
    board = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
             (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
             (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
             (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
             (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
             (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
             (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
             (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
             ]

    def info(self):
        return f'place_board is {self.place_board} and color is {self.color}'

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        elif self.color == "black":
            self.color = "white"
        return self.color

    def change_place(self):
        if self.place_board in self.board:
            return True
        else:
            return False

    def move_pawn(self):
        if self.color == "white":
            (a, b) = self.place_board
            new_pl = (a-1, b)
            if new_pl == self.move:
                return "you can move your`s {} pawn from {} to {}".format(self.color, self.place_board, self.move)
            else:
                return "try another move"
        if self.color == "black":
            (a, b) = self.place_board
            new_pl = (a+1, b)
            if new_pl == self.move:
                return "you can move your`s {} pawn from {} to {}".format(self.color, self.place_board, self.move)
            else:
                return "try another move"

    def move_king(self):
        (a, b) = self.place_board
        new_pl = [(a + 1, b), (a + 1, b + 1), (a + 1, b - 1),
                  (a, b + 1), (a, b - 1),
                  (a - 1, b), (a - 1, b + 1), (a - 1, b - 1)]
        if self.move in new_pl:
            return "you can move your`s King from {} to {}".format(self.place_board, self.move)
        else:
            return "try another move"

    def move_castle(self):
        (a, b) = self.place_board
        new_pl = [(a + 1, b), (a + 2, b), (a + 3, b), (a + 4, b), (a + 5, b), (a + 6, b), (a + 7, b),
                  (a, b + 1), (a, b + 2), (a, b + 3), (a, b + 4), (a, b + 5), (a, b + 6), (a, b + 7),
                  (a - 1, b), (a - 2, b), (a - 3, b), (a - 4, b), (a - 5, b), (a - 6, b), (a - 7, b),
                  (a, b - 1), (a, b - 2), (a, b - 3), (a, b - 4), (a, b - 5), (a, b - 6), (a, b - 7),
                  ]
        if self.move in new_pl:
            return "you can move your`s Castle from {} to {}".format(self.place_board, self.move)
        else:
            return "try another move"

    def move_bishop(self):
        (a, b) = self.place_board
        new_pl = [
            (a + 1, b - 1), (a + 2, b - 2), (a + 3, b - 3), (a + 4, b - 4), (a + 5, b - 5), (a + 6, b - 6),
            (a + 7, b - 7),
            (a - 1, b + 1), (a - 2, b + 2), (a - 3, b + 3), (a - 4, b + 4), (a - 5, b + 5), (a - 6, b + 6),
            (a - 7, b + 7),
            (a - 1, b + 1), (a - 2, b + 2), (a - 3, b + 3), (a - 4, b + 4), (a - 5, b + 5), (a - 6, b + 6),
            (a - 7, b + 7),
            (a + 1, b - 1), (a + 2, b - 2), (a + 3, b - 3), (a + 4, b - 4), (a + 5, b - 5), (a + 6, b - 6),
            (a + 7, b - 7)
            ]
        if self.move in new_pl:
            return "you can move your`s Bishop from {} to {}".format(self.place_board, self.move)
        else:
            return "try another move"

    def move_queen(self):
        (a, b) = self.place_board
        new_pl = [
            (a + 1, b - 1), (a + 2, b - 2), (a + 3, b - 3), (a + 4, b - 4), (a + 5, b - 5), (a + 6, b - 6),
            (a + 7, b - 7),
            (a - 1, b + 1), (a - 2, b + 2), (a - 3, b + 3), (a - 4, b + 4), (a - 5, b + 5), (a - 6, b + 6),
            (a - 7, b + 7),
            (a - 1, b + 1), (a - 2, b + 2), (a - 3, b + 3), (a - 4, b + 4), (a - 5, b + 5), (a - 6, b + 6),
            (a - 7, b + 7),
            (a + 1, b - 1), (a + 2, b - 2), (a + 3, b - 3), (a + 4, b - 4), (a + 5, b - 5), (a + 6, b - 6),
            (a + 7, b - 7),
            (a + 1, b), (a + 2, b), (a + 3, b), (a + 4, b), (a + 5, b), (a + 6, b), (a + 7, b),
            (a, b + 1), (a, b + 2), (a, b + 3), (a, b + 4), (a, b + 5), (a, b + 6), (a, b + 7),
            (a - 1, b), (a - 2, b), (a - 3, b), (a - 4, b), (a - 5, b), (a - 6, b), (a - 7, b),
            (a, b - 1), (a, b - 2), (a, b - 3), (a, b - 4), (a, b - 5), (a, b - 6), (a, b - 7),
        ]
        if self.move in new_pl:
            return "you can move your`s Queen from {} to {}".format(self.place_board, self.move)
        else:
            return "try another move"

    def move_knight(self):
        (a, b) = self.place_board
        new_pl = [(a + 1, b - 2), (a + 2, b - 1), (a - 1, b + 2), (a - 2, b + 1),
                  (a + 1, b + 2), (a + 2, b + 1), (a - 1, b - 2), (a - 2, b - 1)]
        if self.move in new_pl:
            return "you can move your`s Knight from {} to {}".format(self.place_board, self.move)
        else:
            return "try another move"


king = Figure()
king.place_board = (1, 1)
king.color = "black"
king.move = (3, 3)

queen = Figure()
queen.place_board = (1, 8)
queen.color = "black"
queen.move = (1, 3)

castle = Figure()
castle.place_board = (1, 8)
castle.color = "black"
castle.move = (8, 1)

bishop = Figure()
bishop.place_board = (1, 8)
bishop.color = "black"
bishop.move = (8, 1)

knight = Figure()
knight.place_board = (1, 8)
knight.color = "black"
knight.move = (2, 6)

pawn = Figure()
pawn.place_board = (1, 8)
pawn.color = "black"
pawn.move = (1, 2)

print(king.change_color())
print(king.change_place())
print(king.info())
print(king.move_king())
print(knight.move_knight())
