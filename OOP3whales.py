
class Pokemon:
    def __init__(self, name, element, stage, health, energy):
        self._name = name
        self._element = element
        self._stage = stage
        self._hp = health
        self._energy = energy

    def battle_cry(self):
        print(self._name.upper() + '!!!')


class Pichu(Pokemon):

    def thunder_shock(self, target):
        self._energy -= 15
        target._hp -= 40
        print(self._name + ' uses Thunder Shock and deals 40 damage. ' +target._name + ' is left with ' + str(target._hp) + ' HP')

class Pikachu(Pichu):
    def thunderbolt(self, target):
        self._energy -= 30
        target._hp -= 90
        print(self._name + ' uses Thunderbolt and deals 90 damage. ' + target._name + ' is left with ' + str(target._hp) + ' HP')

class Raichu(Pikachu):
    def thunder(self, target):
        self._energy -= 45
        target._hp -= 110
        print(self._name + ' uses Thunder and deals 110 damage. ' + target._name + ' is left with ' + str(target._hp) + ' HP')


pichu = Pichu('Pichu', 'lightning', 1, 200, 200)
pikachu = Pikachu('Pikachu', 'lightning', 2, 350, 400)
raichu = Raichu('Raichu', 'lightning', 3, 600, 800)
pichu.battle_cry()
pikachu.battle_cry()
raichu.battle_cry()
pichu.thunder_shock(pikachu)
pikachu.thunder_shock(pichu)
pikachu.thunderbolt(pichu)
raichu.thunder(pikachu)


'''
class Pill:
    def __init__(self, remedy):
        self.remedy = remedy


pill = Pill('activated coal')
print(pill.remedy)

'''
