'''

class GreatTalent:
    def __init__(self, name, year_of_birth, fav_prog_lang):
        self._name = name
        self._age = 2020 - year_of_birth
        self._fav_prog_lang = fav_prog_lang
        self._year_of_birth = year_of_birth

my_questionnaire = GreatTalent("Din", 2005, "Python")

print("My name is: " + my_questionnaire._name + ",")
print("I am " + str(my_questionnaire._age) + " years old")
print("And my favourite language is " + my_questionnaire._fav_prog_lang + ". I absolutely love it")

'''


class Horse:
    population = 0

    def __init__(self, name, breed, color):
        self._name = name
        self._breed = breed
        self._color = color
        self._hooves = 4
        self.population += 1

    def nicker(self):
        print('*Бешенное игогокания психически неуравновешонной лошади*')

    def hop(self):
        print('Hop-hop-hop')

    def eat(self):
        print('*Звуки агрессивного поедания всего и вся*')

    def kick(self):
        print('*Sound of 5 human bones being broken*')

myhorse = Horse("Betty", "American", "black")
print(myhorse._name)
myhorse.kick()