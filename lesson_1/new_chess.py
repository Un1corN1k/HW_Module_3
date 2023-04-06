from typing import List, Tuple


def check_if_in_board(new_position: Tuple[int, int]) -> bool:
    x, y = new_position
    return 0 <= x <= 7 and 0 <= y <= 7


class Figure:
    _color: str = "white"
    _position: tuple = (1, 1)

    def info(self):
        return 'place_board is {} and color is {}'.format(self._position, self._color)

    def set_position(self, new_position):
        if check_if_in_board(new_position):
            self._position = new_position
        else:
            print("Not on board")

    def change_color(self):
        if self._color == "white":
            self._color = "black"
        elif self._color == "black":
            self._color = "white"

    def move(self, position: tuple) -> bool:
        raise NotImplementedError


class Rook(Figure):
    def move(self, position: tuple) -> bool:
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        delta = curr_x - new_x, curr_y - new_y
        if 0 in delta:
            self.set_position(position)
            return position


class Bishop(Figure):
    def move(self, position: tuple):
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        if abs(new_x - curr_x) == abs(new_y - curr_y):
            self.set_position(position)
            return position


class Queen(Figure):
    def move(self, position: tuple) -> bool:
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        delta = curr_x - new_x, curr_y - new_y
        x, y = delta
        if x == y or 0 in delta:
            self.set_position(position)
            return position


class King(Figure):
    def move(self, position: tuple) -> bool:
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        if abs(new_x - curr_x) <= 1 and abs(new_y - curr_y) <= 1:
            self.set_position(position)
            return position


class Pawn(Figure):
    def move(self, position: tuple) -> bool:
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        if (self._color == "white" and new_y == curr_y + 1 and new_x == curr_x) or (
                self._color == "black" and new_y == curr_y - 1 and new_x == curr_x):
            self.set_position(position)
            return position


class Knight(Figure):
    def move(self, position: tuple) -> bool:
        if not check_if_in_board(position):
            return False
        new_x, new_y = position
        curr_x, curr_y = self._position
        x_delta = curr_x - new_x
        y_delta = curr_y - new_y
        if (x_delta == 1 and y_delta == 2) or (x_delta == 2 and y_delta == 1):
            self.set_position(position)
            return position


def get_figures_which_can_move(figures_to_check: List[Figure], position: tuple) -> List[Figure]:
    return [figure for figure in figures_to_check if figure.move(position)]


pawn1 = Pawn()
pawn2 = Pawn()
pawn3 = Pawn()
king1 = King()
king2 = King()
king3 = King()
rook1 = Rook()
rook2 = Rook()
rook3 = Rook()
bishop1 = Bishop()
bishop2 = Bishop()
bishop3 = Bishop()
queen1 = Queen()
queen2 = Queen()
queen3 = Queen()
knight1 = Knight()
knight2 = Knight()
knight3 = Knight()

pawn1.set_position((3, 3))
king2.set_position((4, 4))
bishop2.set_position((6, 1))
knight3.set_position((5, 5))
queen1.set_position((3, 7))
pawn2.change_color()
pawn2.set_position((3, 5))

figures = [pawn1, pawn2, pawn3, queen1, queen2, queen3, king1, king2, king3, bishop1, bishop2, bishop3, rook1, rook2,
           rook3, knight1, knight2, knight3]

result = get_figures_which_can_move(figures, (3, 4))
print(result)
