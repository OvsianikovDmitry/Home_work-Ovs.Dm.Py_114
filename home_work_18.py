class Tomato:

    states = {1:'нет', 2:'цветёт', 3:'зелённый', 4:'красный'}

    def __init__(self,index):
        self._index = index
        self._state = 1


    def grow(self):
        if self._state <= 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False


class TomatoBush(Tomato):

    def __init__(self,quantity):
        self.tomatoes = [Tomato(index) for index in range(quantity)]



    def grow_all(self):

        for i in self.tomatoes:
            i.grow()


    def all_are_ripe(self):

        for i in self.tomatoes:
            return i.is_ripe()



    def give_away_all(self):
        print('Урожай собран')
        self.tomatoes.clear()


class Gardener:

    def __init__(self,name,TomatoBush_obj):
        self.name = name
        self._plant = TomatoBush_obj

    def work(self):
        self._plant.grow_all()
        print('work')

    def harvest(self):
        if self._plant.all_are_ripe() == True:
            self._plant.give_away_all()
        else:
            print('Не все поспели')




    @staticmethod
    def knowleadge_base():
        print(f'Справка')


Gardener.knowleadge_base()
tomat = TomatoBush(10)
gardener = Gardener('Dmitry',tomat)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()


