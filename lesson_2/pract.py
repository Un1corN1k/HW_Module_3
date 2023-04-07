CUP_SIZE_WATER = 150
CUP_SIZE_BEANS = 50


class CoffeMachine:
    _water = 0
    _beans = 0
    _max_water = 1000
    _max_beans = 500

    def get_water(self):
        return self._water

    def get_beans(self):
        return self._beans

    def feel_water(self, amount_w):
        if amount_w + self._water <= self._max_water:
            self._water += amount_w
        else:
            self._water = self._max_water

    def feel_beans(self, amount_b):
        if amount_b + self._beans <= self._max_beans:
            self._beans += amount_b
        else:
            self._beans = self._max_beans

    def make_coffee(self, cups):
        if self._beans >= CUP_SIZE_BEANS * cups and self._water >= CUP_SIZE_WATER * cups:
            self._beans -= CUP_SIZE_BEANS * cups
            self._water -= CUP_SIZE_WATER * cups
            print("Take you coffee")
        else:
            print("Not enough ingredients")


italian = CoffeMachine()
usa = CoffeMachine()

italian.feel_water(500)

usa.feel_water(500)
usa.feel_water(500)

usa.feel_beans(300)

italian.feel_beans(300)

italian.make_coffee(2)
usa.make_coffee(20)


def poor_water(lst_machines, ml):
    return sum(m.get_water() for m in lst_machines) > ml


print(poor_water([italian, usa], 500))
