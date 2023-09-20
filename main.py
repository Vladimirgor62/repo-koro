class Dogs:
    def __init__ (self, dogsname, age, breed):
        self. dogsname = dogsname
        self._age = age
        self. breed = breed
    def presentation(self):
        return f'Перед Вами собака {self.dogsname} {self._age} лет, порода {self.breed}'
dog1=Dogs('Recs', 9, 'shepherd')
dog2=Dogs('Sharic', 3, 'dalmatian')
print(dog2.dogsname, dog2._age, dog2.breed)
print(dog1.dogsname, dog1._age, dog1.breed)
class Winner(Dogs):#
    def __init__(self, dogsname, age, breed,suit):
        super().__init__(dogsname, age, breed)
        self.suit = suit
winner1=Winner('Wert',5, 'bulldog', 'red')
print(winner1.suit)
print(winner1.presentation())
class Purpose(Winner):
    def __init__(self, dogsname, age, breed, suit, purpos ):
        super().__init__(self, dogsname, age, breed,)
        self.purpos = purpos
        self.suit = suit
dogwinner=Purpose('Wert',5, 'bulldog', 'red', 'hunter')

print(dogwinner.__getstate__())
