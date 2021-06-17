'''Создайте класс Factory и внутри создайте 2 метода:

Метод engine который возвращает строку "Двигатель создан"

Метод bridge который возвращает строку "Ходовая часть создана"'''

class Factory:

	def engine(self):
		return("Двигатель создан")

	def bridge(self):
		return("Ходовая часть создана")

class Toyota(Factory):

	def wheels(self):
		return("Колеса готовы")

	def windows(self):
		return("Стекла готовы")

t = [Toyota().engine(), Toyota().bridge(), Toyota().wheels(), Toyota().windows()]

print(t)
