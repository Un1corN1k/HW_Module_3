from typing import Any, List


def _check_if_in_board(new_place: tuple) -> bool:
    if all(0 < place <= 8 for place in new_place):
        return True
    else:
        print('Cannot use this place')
        return False


class Figure:
    _color: str = "white"
    _place: tuple = (1, 1)

    def info(self) -> str:
        return f'place_board is {self._place} and color is {self._color}'

    def change_color(self) -> None:
        if self._color == "white":
            self._color = "black"
        elif self._color == "black":
            self._color = "white"

    def change_place(self, new_place: tuple) -> None:
        if _check_if_in_board(new_place):
            self._place = new_place

    def check_move(self, new_place: tuple) -> Any:
        if _check_if_in_board(new_place):
            raise NotImplementedError


class Pawn(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        return (self._color == "white" and new_vertical == old_vertical + 1 and new_horizontal == old_horizontal) or (
                    self._color == "black" and new_vertical == old_vertical - 1 and new_horizontal == old_horizontal)


class King(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        return abs(new_horizontal - old_horizontal) <= 1 and abs(new_vertical - old_vertical) <= 1


class Rook(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        return old_vertical == new_vertical or old_horizontal == new_horizontal


class Bishop(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        return abs(new_vertical - old_vertical) == abs(new_horizontal - old_horizontal)


class Queen(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        as_bishop = abs(new_vertical - old_vertical) == abs(new_horizontal - new_horizontal)
        as_rook = old_vertical == new_vertical or old_horizontal == new_horizontal
        return as_rook or as_bishop


class Knight(Figure):
    def check_move(self, new_place: tuple) -> bool:
        old_horizontal, old_vertical = self._place
        new_horizontal, new_vertical = new_place
        vertical_diff = abs(old_vertical - new_vertical)
        horizontal_diff = abs(old_horizontal - new_horizontal)
        return (vertical_diff == 1 and horizontal_diff == 2) or (vertical_diff == 2 and horizontal_diff == 1)


def get_figures_which_can_move(figures_to_check: List[Figure], new_place: tuple) -> List[Figure]:
    return [figure for figure in figures_to_check if figure.check_move(new_place)]


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

pawn1.change_place((3, 3))
king2.change_place((4, 4))
bishop2.change_place((6, 1))
knight3.change_place((5, 5))
queen1.change_place((3, 7))
pawn2.change_color()
pawn2.change_place((3, 5))

figures = [pawn1, pawn2, pawn3, queen1, queen2, queen3, king1, king2, king3, bishop1, bishop2, bishop3, rook1, rook2,
           rook3, knight1, knight2, knight3]

result = get_figures_which_can_move(figures, (3,4))