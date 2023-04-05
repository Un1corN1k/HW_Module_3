class Phone:
    _counter: int = 0
    description: str = "Nobody"
    ph_number: str = "+380000000000"

    def change_number(self, ph_number) -> str:
        self.ph_number = ph_number

    def description_call(self, description) -> str:
        self.description = description

    def count_callings(self) -> int:
        return self._counter

    def accept_call(self) -> int:
        self._counter += 1

    def __repr__(self):
        return f'You have {self._counter} call from {self.description}, whose number {self.ph_number}'


lst_my = ["Sasha", "+380678435125"]
lst_his = ['Oleg', '+380953475243']
lst_her = ['Diana', '+380503247002']

my_ph = Phone()
his_ph = Phone()
her_ph = Phone()

my_ph.change_number(lst_my[1])
my_ph.description_call(lst_my[0])
my_ph.accept_call()
my_ph.accept_call()
my_ph.accept_call()

his_ph.change_number(lst_his[1])
his_ph.description_call(lst_his[0])
his_ph.accept_call()
his_ph.accept_call()
his_ph.accept_call()
his_ph.accept_call()

her_ph.description_call(lst_her[0])
her_ph.change_number(lst_her[1])
her_ph.accept_call()
her_ph.accept_call()
her_ph.accept_call()

print(my_ph)
print(his_ph)
print(her_ph)


def answering_machine(lst_ph: tuple) -> int:
    return sum(i.count_callings() for i in lst_ph)


print(answering_machine([my_ph, his_ph, her_ph]))
