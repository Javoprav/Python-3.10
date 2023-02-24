'''16. ⚙️ Бутылки
16 из 26
Создай класс Bottle (бутылка) c полями

Цвет (color) - строка
Объем (volume) - число с плавающей точкой
Создай три экземпляра

Красная 0.7
Белая 0.3
Черная 1.0'''

class Bottle:

	def __init__(self, color, volume):
		self.color = color
		self.volume = volume

bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle("Белая", 0.3)
bottle_3 = Bottle("Черная", 1.0)

print(bottle_1.color, bottle_1.volume)
print(bottle_2.color, bottle_2.volume)
print(bottle_3.color, bottle_3.volume)

'''19. ⚙️ Бутылки 2
19 из 26
Создай класс Bottle (бутылка) c полями

Цвет (color) - строка
Содержимое в мл (contains) - число с плавающей точкой
При инициализации класса, поле 
contains
 устанавливается = 0

Создай два экземпляра класса

Красная
Синяя
Добавь классу 
Bottle
 метод 
get_content
 который вернет актуальное количество жидкости внутри в виде числа с плавающей точкой.

Добавь классу 
Bottle
 метод 
fill(volume)
 который увеличит 
contains
 на указанный объем.'''

class Bottle:
  def __init__(self, color, contains = 0):
    self.color = color
    self.contains = contains

  def get_content(self):
    return float(self.contains)

  def fill(self, volume):
    self.contains = volume
    
bottle_1 = Bottle('Красная')
bottle_2 = Bottle('Синяя')

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())


'''20. ⚙️ Список дел
20 из 26
Создай класс TodoList у которого есть поле задачи 
tasks
 – список строк)

При инициализации список задач будет пустым.

Добавь к классу метод 
add_task(<название задачи>)
 который добавляет задачу в список

Создай переменную todo_list – экземпляр класса TodoList c задачами:

Выключить свет
Поменять лампочку
Включить свет'''

class TodoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, tasks):
    self.tasks.append(tasks) 


todo_list = TodoList()
todo_list.add_task('Выключить свет')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Включить свет')

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))

'''21. ⚙️ Игрок и его баллы
21 из 26
Создай класс 
Player
 с полями:
Имя игрока (name) – строка
Количество очков (score) – целое число, при инициализации всегда 0
Добавь классу метод get_score() который возвращает значение score

Добавь классу метод 
set_score(<значение>) который задает значение, например, set_score(20).

Создай экземпляр класса 
Player c именем Алиса'''

class Player:
  def __init__(self, name, score = 0):
    self.name = name
    self.score = score

  def get_score(self):
    return self.score

  def set_score(self, score):
    self.score = score

player_1 = Player('Алиса')

print(player_1.name, player_1.get_score()) 
player_1.set_score(200)
print(player_1.name, player_1.get_score()) 
player_1.set_score(500) 
print(player_1.name, player_1.get_score())

'''22. ⚙️ Номера
22 из 26
Создай класс Number c полем value (указывается при инициализации)
Добавь методы:
.get() возвращает текущее value
.add(<значение>) добавляет указанное число к value
.subtract(<значение>) вычитает указанное число из value'''

class Number:
    def __init__(self, value):
        self.value = value
    def get(self):
        return self.value
    def add(self, value):
        self.value += value
    def subtract(self, value):
        self.value -= value

x = Number(7)
x.add(3)
x.subtract(10)
x.get()


n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())

'''23. ⚙️ Круг
23 из 26
Создай класс Circle, с полем radius(указывается при инициализации)
Добавь методы:
get_radius()- возвращает радиус
get_diameter()- возвращает двойной радиус
get_perimeter()- возвращает 2*радиус*Пи (можно использовать pi=3.14 или math.pi)'''

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def get_diameter(self):
        return self.radius * 2
    def get_perimeter(self):
        return 2 * self.radius * math.pi


circle_1 = Circle(7)
print("радиус", circle_1.get_radius() )
print("диаметр", circle_1.get_diameter() )
print("периметр", round(circle_1.get_perimeter(),1))


'''24. ⚙️ Квадрат
24 из 26
Создай класс Square с полями
Длина строны (side_length) – целое число
Цвет (color) – строка, поле опциональное и равно по умолчанию white
Добавить методы:
set_side(length) – задает размер стороны
set_color(color) - задает цвет
get_side() - возвращает 
side_length в виде целого числа
get_color() - возвращает color
get_perimeter() - возвращает периметр (строну * 4)'''

class Square:
  def __init__(self, side_length, color = 'white'):
    self.side_length = side_length
    self.color = color
    
  def set_side(self, length):
    self.side_length = length
  
  def set_color(self, color):
    self.color = color
  
  def get_side(self):
    return self.side_length
  
  def get_color(self):
    return self.color
  
  def get_perimeter(self):
    return self.side_length * 4
    
square_1 = Square(2)
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1.set_side(3)
square_1.set_color("red")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1 = Square(1, "black")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())

'''25. ⚙️ Классы
25 из 26
У вас есть класс 
Room
 c полями

Номер номера (
number
) – целое число

Свободно ли (
is_free
) – булев тип

Допишите функцию, которая перебирает список номеров и возвращает список свободных номеров (список экземпляров класса Room).'''

class Room:

    def __init__(self, number, is_free):
      self.number = number
      self.is_free = is_free
        
    def get_is_free(self):
      return self.is_free

    def get_number(self):
      return self.number
    
def get_free_rooms(rooms):
    free_rooms = []
    for i in rooms:
      if i.get_is_free() == True:
        free_rooms.append(i)
    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)

[print(r.number) for r in rooms_free]

'''8. ⚙️ Общие корни
8 из 13
У предоставленных двух классов создайте общего родителя 
Character
, вынесите туда логику передвижения, а 
init
 оставьте у каждого свой.

Вывод при этом не должен поменяться.'''

class Character():
  def __init__(self, name):
    self.name = name
    
  def move(self, direction, distance):
    if direction == "north":
      print(self.name, "движется", distance, "метров", "на север")
    elif direction == "south":
      print(self.name, "движется", distance, "метров", "на юг")
    elif direction == "west":
      print(self.name, "движется", distance, "метров", "на запад")
    elif direction == "east":
      print(self.name, "движется", distance, "метров", "на восток")
    else:
      print(self.name, "движется непонятно куда")
  

class Hero():

  def __init__(self, name):
    self.name = name

  def move(self, direction, distance):

    if direction == "north":
      print(self.name, "движется", distance, "метров", "на север")
    elif direction == "south":
      print(self.name, "движется", distance, "метров", "на юг")
    elif direction == "west":
      print(self.name, "движется", distance, "метров", "на запад")
    elif direction == "east":
      print(self.name, "движется", distance, "метров", "на восток")
    else:
      print(self.name, "движется непонятно куда")


class Enemy():

  def __init__(self, name):
    self.name = name

  def move(self, direction, distance):

    directions_list = {"north":"на север", "south": "на юг", "west": "на запад", "east": "на восток"}
    if direction not in directions_list.keys():
      print(self.name, "движется непонятно куда")  
    else:
      print(self.name, "движется", distance, "метров", directions_list[direction])     


pythomir = Hero("Питомир")
bugoonya = Enemy("Багуня")

pythomir.move("north", 50)
pythomir.move("west", 10)
pythomir.move("climb", 0)

bugoonya.move("north", 50)
bugoonya.move("west", 10)
pythomir.move("climb", 0)

# Не удаляйте код ниже, это проверка!

if not 'Character' in dir():
 print("Общий класс родитель Character не создан")

if not hasattr(Character, "move"):
 print("У общего класса отсутствует метод move")

'''9. ⚙️ Злые наследники
9 из 13
Унаследуйте от класса 
Enemy
 класс 
Dragon
.

Добавьте дочернему классу методы:

bite
 (выводит "я кусаюсь"),

burn
 (выводит "я дышу огнем").'''

class Enemy():

  def __init__(self, name, health):

    self.is_alive = True;
    self.name = name
    self.health = health

class Dragon(Enemy):
  def bite(self):
    print("я кусаюсь")
  def burn(self):
    print("я дышу огнем")

dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()

'''10. ⚙️ Представительный класс
10 из 13
У нас есть класс
Hero
 и 
hero
 — экземляр класса 
Hero
.

При выполнении 
print(hero)
 должна выводиться информация про 
hero
 в формате:

Герой Питомир взял с собой меч, плащ, шляпа

Реализуйте магический метод 
repr
.

Формат вывода:

Герой Питомир взял с собой меч, плащ, шляпа'''

class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions

  def __repr__(self):
    return f"Герой {self.name} взял с собой {', '.join(self.posessions)}"

hero = Hero("Питомир", ["меч", "плащ", "шляпа"]) 
print(hero)

'''12. ⚙️ Финальная задача про ящики
12 из 13
Опишите класс 
Box
, у которого будут свойства:

size
weight
contains
и метод 
observe()
, который возвращает:

Это похоже на ящик размером 30x30 и весом 35кг

Наследуйте от него класс 
Container
.

Он будет отличаться наличием метода 
open()
, который возвращает то, что лежит в ящике, например:

В ящике размером 40x40 и весом 1кг оказалось 4 кг апельсин

Создайте экземпляр 
box_1
 с размерами 30x30, весом 1 и содержимым "15 золотых монет".

Создайте экземпляр 
container_1
 с размерами 50x30, весом 2 и содержимым "7 золотых монет".'''

class Box():

    def __init__(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains

    def observe(self):
        return f'Это похоже на ящик размером {self.size} и весом {self.weight}кг'


class Container(Box):

    def open(self):
        return f'В ящике размером {self.size} и весом {self.weight}кг оказалось {self.contains}'


box_1 = Container('30x30', 1, "15 золотых монет")
# box_1.observe('30x30', 1, "15 золотых монет")
container_1 = Container('50x30', 2, "7 золотых монет")
# container_1.open('50x30', 2, "7 золотых монет")

try: Box
except: print("Класс Box не задан")
try: Container
except: print("Класс Container не задан")
try: Container.open
except: print("Метод open у Container не задан или с ошибкой")
try: Container.observe
except: print("Метод observe у Container не наследуется или с ошибкой")
try: box_1
except: print("Экземпляр box_1 не существует")
try: container_1
except: print("Экземпляр container_1 не существует")

print(container_1.observe())
print(container_1.open())