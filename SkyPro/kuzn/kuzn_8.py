'''### Тренажер: Бутылки 1

Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Объем (volume) - число с плавающей точкой

Создай три экземпляра

- Красную 0.7
- Белую 0.3
- Черную 1,0'''

class Bottle:
  
  def __init__(self, color, volume):
    self.color = color
    self.volume = volume

  def __repr__(self):
    return f"Бутылка {self.color}, {self.volume}"

botle_1 = Bottle('Красную', 0.7)
botle_2 = Bottle('Белую', 0.3)
botle_3 = Bottle('Черную', 1.0)

print(botle_1.color, botle_1.volume)
print(botle_2.color, botle_2.volume)
print(botle_3.color, botle_3.volume)

'''### Тренажер: Студенты

Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]'''

class Student:

  def __init__(self, name, course):
    self.name = name
    self.course = course

alice = Student('Алиса' , '3 [курс]')
margo = Student('Маргарита' , '2 [курс]')

print(alice.name, alice.course)
print(margo.name, margo.course)

'''### Тренажер: Альбом

Создай класс Album у которого есть поля 

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou'''

class Album:
  def __init__(self, artist, title, tracks):
    self.artist = artist
    self.title = title
    self.tracks = tracks

album_1 = Album('Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])
album_2 = Album('Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])

print(album_1.artist, album_1.title, f'{len(album_1.tracks)} теркa')
print(album_2.artist, album_2.title, f'{len(album_2.tracks)} теркa')

"""### Тренажер: Бутылки 2

Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Содержимое в мл (contains) -  число с плавающей точкой

При инициализации класса, поле `contains` устанавливается = 0

Создай два экземпляра класса

- Красная
- Синяя

Добавь классу `Bottle` метод `get_content` который вернет актуальное количество жидкости внутри в виде  числа с плавающей точкой.

Добавь классу `Bottle` метод `fill(volume)` который увеличит `contains` на указанный объем."""

class Bottle:
  def __init__(self, color, contains=0):
    self.color = color
    self.contains = contains

  def get_content(self):
    return self.contains

  def fill(self, volume):
    self.contains += volume


bottle_1 = Bottle('Красная')
bottle_2 = Bottle('Синяя')
  

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())

'''### Тренажер: список дел

Создай класс TodoList у которого есть поле задачи (`tasks`) – список строк)

При инициализации список задач будет пустым.

Добавь к классу метод `add_task(<название задачи>)` который добавляет задачу в список

Создай переменную todo_list – экземпляр класса TodoList c задачами:
Купить лампочку
Поменять лампочку
Выкинуть лампочку'''

class TodoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

todo_list = TodoList()
todo_list.add_task("Купить лампочку")
todo_list.add_task("Выключить свет") 
todo_list.add_task("Поменять лампочку")
todo_list.add_task("Включить свет")
print(" ".join(todo_list.tasks))

'''### Тренажер: Игрок и его баллы

Создай класс `Player` с полями 

Имя игрока (`name`) – строка

Количество очков (`score`) – целое число, при инициализации всегда 0

Добавь классу метод `get_score()` который возвращает значение `score`

Добавь классу метод `set_score(<значение>)` который задает значение, например, `set_score(20)`.

Создай экземпляр класса `Player` c именем `Алиса`'''

class Player:

  def __init__(self, name, score=0):
    self.name = name
    self.score = score
    
  def get_score(self):
    return self.score

  def set_score(self, score):
    self.score = score
 
player_1 = Player('Алиса')
  
# Не удаляйте этот код, он нужен для проверки

print(player_1.name, player_1.get_score()) 
player_1.set_score(200)
print(player_1.name, player_1.get_score()) 
player_1.set_score(500) 
print(player_1.name, player_1.get_score())

'''### Тренажер: номера

Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value'''

class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, value):
        self.value = value

    def substract(self, value_min):
        self.value -= value_min

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.substract(5)
print(n.get())

'''### Классы, задача 11
Создай класс Room c полями 
`number` - число
`type` - строка
`price` - число с точкой
Создайте несколько элементов и положите их словарь
12
standard
2000
13
standard
2000
14
joint
2500
15
suite
3000
Структура словаря
{12: class_instance, 13: class_instance, 14: class_instance}
Обработайте запрос с номером номера и выведите информацию о номере, типе и цене
Входные данные
```
13
```
Пример вывода: 
Номер: 13
Тип номера: standard
Цена за сутки: 2000'''

class Room:
  def __init__(self, number, type, price):
    self.number = number
    self.type = type
    self.price = price
    
  def get_room(self):
    return f'Номер: {self.number} \nТип номера: {self.type} \nЦена за сутки: {self.price}'

n_12 = Room(12, 'standard', 2000.00)
n_13 = Room(13, 'standard', 2000.00)
n_14 = Room(14, 'joint', 2500.00)
n_15 = Room(15, 'suite', 3000.00)

numbers = {12 : n_12.get_room(), 13 : n_13.get_room(), 14 : n_14.get_room(), 15 : n_15.get_room()}

inp = int(input('Ввод: '))
print(numbers[inp])

'''### Классы задача 12
Создайте класс Bottle c полями `color`, `volume`
**Методы класса:** 
`get_color()` – вернет цвет
`get_volume()` - вернет объем налитого
Создайте класс Shelve с полями 
`bottles` (типа список), изначально пустое
**Методы класса:** 
`add_bottle(bottle)` - принимает экземпляр класса bottle, добавляет элемент к списку bottles у экземпляра класса Shelve
`get_number_of_bottles()` - возвращает количество бутылочек как целое число'''

class Bottle:
  def __init__(self, color, volume):
    self.color = color
    self.volume = volume

  def get_color(self):
    return self.color

  def get_volume(self):
    return self.volume

class Shelve(Bottle):
  def __init__(self, bottles=[]):
    self.bottles = bottles

  def add_bottle(self, bottle):
    self.bottles.append(bottle)

  def get_number_of_bottles(self):
    return len(self.bottles)

bottle_1 = Bottle("Квандричневый", 0.2)
bottle_2 = Bottle("Чебурашковый", 0.2)

print(bottle_2.color, bottle_2.volume)
print(bottle_2.get_color())
print(bottle_1.color, bottle_1.volume)
print(bottle_1.get_color())

bottle_2.add_bottle(bottle_1, bottle_2)
print(bottle_2.get_number_of_bottles())

'''### Классы задача 12
Создайте класс Bottle c полями `color`, `volume`
**Методы класса:** 
`get_color()` – вернет цвет
`get_volume()` - вернет объем налитого
Создайте класс Shelve с полями 
`bottles` (типа список), изначально пустое
**Методы класса:** 
`add_bottle(bottle)` - принимает экземпляр класса bottle, добавляет элемент к списку bottles у экземпляра класса Shelve
`get_number_of_bottles()` - возвращает количество бутылочек как целое число'''

class Bottle:
  def __init__(self, color, volume):
    self.color = color
    self.volume = volume

  def get_color(self):
    return self.color

  def get_volume(self):
    return self.volume

class Shelve(Bottle):
    bottles=[]

    def add_bottle(self):
      Shelve.bottles.append(self)

    def get_number_of_bottles():
      return len(Shelve.bottles)

bottle_1 = Bottle("Квандричневый", 0.2)
bottle_2 = Bottle("Чебурашковый", 0.2)

print(bottle_2.color, bottle_2.volume)
print(bottle_2.get_color())
print(bottle_1.color, bottle_1.volume)
print(bottle_1.get_color())

Shelve.add_bottle(bottle_1)
Shelve.add_bottle(bottle_2)
print(Shelve.get_number_of_bottles())
print(Shelve.bottles)