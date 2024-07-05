class Superhero:

    people = 'people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    def nameprint(self):
        return f'name: {self.name}'

    def health_point_x2(self):
        return f'new health points: {self.health_point * 2}'

    def __str__(self):
        return f'nickname:{self.nickname}; superpower: {self.superpower}; health points: {self.health_point};'

    def __len__(self):
        return len(self.catchphrase)


class AirHero(Superhero):

    people = 'people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase, fly=False):
        Superhero.__init__(self, name, nickname, superpower, health_point, catchphrase)
        self.fly = fly

    def health_point_x2(self):
        return f'new health points: {self.health_point ** 2}'




timur = Superhero('timur', 'Gngng', 'wowosurprice', 100, 'yaaaay')

print(timur.nameprint())
print(timur.__len__())
print(timur.__str__())
print(timur.health_point_x2())
