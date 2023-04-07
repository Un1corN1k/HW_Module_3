from typing import List, Tuple


def within_board(new_position: Tuple[int, int]) -> bool:
    x, y = new_position
    return 0 <= x <= 7 and 0 <= y <= 7


class Figure:
    _color: str = "white"
    _position: tuple = (1, 1)

    def info(self):
        return 'place_board is {} and color is {}'.format(self._position, self._color)

    def set_position(self, new_position):
        if within_board(new_position):
            self._position = new_position
        else:
            print("Not on board")

    def change_color(self):
        if self._color == "white":
            self._color = "black"
        elif self._color == "black":
            self._color = "white"

    def can_move(self, position: tuple) -> bool:
        raise NotImplementedError

    def get_delta(self, position: Tuple[int, int]) -> Tuple[int, int]:
        new_x, new_y = position
        curr_x, curr_y = self._position

        return curr_x - new_x, curr_y - new_y


class Rook(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            return dx == 0 or dy == 0


class Bishop(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            return abs(dx) == abs(dy)


class Queen(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            return(abs(dx) == abs(dy)) or (dx == 0 or dy == 0)


class King(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            return dx <= 1 and dy <= 1


class Pawn(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            if self._color == "black" and (dx == 0 and dy == 1):
                return True
            if self._color == "white" and (dx == 0 and dy == -1):
                return True


class Knight(Figure):
    def can_move(self, position: tuple) -> bool:
        if within_board(position):
            dx, dy = self.get_delta(position)
            return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


def get_figures_which_can_move(figures_to_check: List[Figure], position: tuple) -> List[Figure]:
    return [figure for figure in figures_to_check if figure.can_move(position)]


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
pawn3.set_position((4, 3))
king1.set_position((5, 4))
king2.set_position((4, 4))
king3.set_position((4, 6))
rook3.set_position((7, 7))
rook2.set_position((3, 7))
rook1.set_position((7, 4))
bishop1.set_position((6, 1))
bishop2.set_position((6, 5))
bishop3.set_position((6, 7))
knight1.set_position((3, 5))
knight2.set_position((5, 5))
knight3.set_position((5, 7))
queen1.set_position((3, 7))
queen2.set_position((1, 4))
queen1.set_position((3, 3))
pawn2.change_color()
pawn2.set_position((3, 5))

figures = [pawn1, pawn2, pawn3, queen1, queen2, queen3, king1, king2, king3, bishop1, bishop2, bishop3, rook1, rook2,
           rook3, knight1, knight2, knight3]

result = get_figures_which_can_move(figures, (3, 4))
print(result)
