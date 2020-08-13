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
