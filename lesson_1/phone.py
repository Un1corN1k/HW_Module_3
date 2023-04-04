class Phone:
    _counter = 0
    description = ""
    ph_number = " "

    def change_number(self, ph_number ):
        self.ph_number = ph_number
        return ph_number

    def output_count_callings(self):
        return self._counter

    def count_callings(self):
        self._counter += 1
        return self._counter


lst = ["Sasha", "+380678435125"]
my_ph = Phone()
my_ph.count_callings()
my_ph.count_callings()
my_ph.ph_number = lst[1]
my_ph.description = lst[0]
my_out_ph = my_ph.output_count_callings()


lst = ["Oleg", "+380954123678"]
my_ph1 = Phone()
my_ph1.count_callings()
my_ph1.count_callings()
my_ph1.count_callings()
my_ph1.count_callings()
my_ph1.ph_number = lst[1]
my_ph1.description = lst[0]
my_out_ph1 = my_ph1.output_count_callings()


lst = ["Dmitro", "+380507823478"]
my_ph2 = Phone()
my_ph2.count_callings()
my_ph2.count_callings()
my_ph2.count_callings()
my_ph2.count_callings()
my_ph2.count_callings()
my_ph2.count_callings()
my_ph2.ph_number = lst[1]
my_ph2.description = lst[0]
my_out_ph2 = my_ph2.output_count_callings()


def answering_machine():
    list_ph = (my_ph.ph_number, my_ph1.ph_number, my_ph2.ph_number)
    list_description = (my_ph.description, my_ph1.description, my_ph2.description)
    list_out_ph = (my_out_ph, my_out_ph1, my_out_ph2)
    answer = zip(list_description, list_ph, list_out_ph)
    out_call = sum(list_out_ph)
    print([f'{d} called you, his phone number {ph}, you have {out} missed calls.' for d, ph, out in answer])
    print('Total you have ', out_call, ' missed calls.')


print(answering_machine())