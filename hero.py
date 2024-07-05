class SuperHero:

    people = 'people'

    def __init__(self, name, nickname, superpower, healthpoints, catchphrase):

        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.healthpoints = healthpoints
        self.catchphrase = catchphrase

    def nameprint(self):
        return f'name of hero:{self.name}'

    def healthpoint_sqare(self):
        return self.healthpoints * 2

    def __str__(self):
        return f'nickname:{self.nickname}\nsuperpower:{self.superpower}\n{self.healthpoints}'

    def __len__(self):
        return len(self.catchphrase)


superman = SuperHero('Ken', 'Super-Man', 'better than normal person', 1000, 'Hello there')

print(superman.nameprint())
print(superman.healthpoint_sqare())
print(superman.__str__())
print(superman.__len__())


class EarthHero(SuperHero):

    def __init__(self, name, nickname, superpower, healthpoints, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, healthpoints, catchphrase)
        self.damage = damage
        self.fly = fly

    def healthpoint_sqare(self):
        return f'{self.fly != True}, {self.healthpoints ** 2}'

    def true_phrase(self):
        return f'True\n'



flash = EarthHero('Flash', 'Flash', 'fast as hell', 300, 'hello dummies', 100)
print(flash.healthpoint_sqare())
print(flash.true_phrase())


class Villian(EarthHero):

    people = 'monster'

    def __init__(self, name, nickname, superpower, healthpoints, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, healthpoints, catchphrase, damage, fly=False)
        pass

    def gen_x(self): ...

    def crit(self):
        return f'CRITICAL DAMAGE:{self.damage ** 2}'


michle = Villian('Michel', 'Michel Maiers', 'immortal', 100000000, 'None', 1000)

print(Villian.crit(flash))
