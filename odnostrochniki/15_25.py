# 15
lst = [x**2 for x in range(10)] # создания списка квадратов чисел
print(lst)

# 16

# До
squares = []
for i in range(10):
 squares.append(i**2)
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# После
print([i**2 for i in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 23

x = 1 > 2
print(x)
# False
y = 2 > 1
print(y)
# True

#     \n, символ пробела \s и символ табуляции \t.

                                              # 25 

#                                            Строковые типы данных
## Важнейшие методы для работы со строками
y = " This is lazy\t\n "
print(y.strip())
# Удаляем пробелы: 'This is lazy'
print("DrDre".lower())
# В нижнем регистре: 'drdre'
print("attention".upper())
# В верхнем регистре: 'ATTENTION'
print("smartphone".startswith("smart"))
# Сопоставляет префикс строки с аргументом: True
print("smartphone".endswith("phone"))
# Сопоставляет суффикс строки с аргументом: True
print("another".find("other"))
# Индекс найденного вхождения: 2
print("cheat".replace("ch", "m"))
# Заменяет все вхождения первого аргумента на второй: meat
print(','.join(["F", "B", "I"]))
# Склеивает все элементы списка, используя строку-разделитель: F,B,I
print(len("Rumpelstiltskin"))
# Длина строки: 15
print("ear" in "earth")
# Содержится: True

                                                 # 28

# 1. Добавление в конец списка
l = [1, 2, 2]
l.append(4)
print(l)
# [1, 2, 2, 4]
# 2. Вставка
l = [1, 2, 4]
l.insert(2, 3)
print(l)
# [1, 2, 3, 4]
# 3. Конкатенация списков
print([1, 2, 2] + [4])
# [1, 2, 2, 4]

                                                   # 29

#   extend()   # Он служит для добавления в конец списка нескольких элементов сразу наиболее эффективным способом.

l = [1, 2, 2, 4]
l.remove(1)
print(l)
# [2, 2, 4]

'''Инвертирование списков
Порядок элементов списка можно инвертировать с помощью метода list.reverse():'''
l = [1, 2, 2, 4]
l.reverse()
print(l)
# [4, 2, 2, 1]

'''Сортировка списков
Отсортировать элементы списка можно с помощью метода list.sort():'''
l = [2, 1, 4, 2]
l.sort()
print(l)
# [1, 2, 2, 4]

l = ['b', 'a']
l.reverse()
print(l) # ['a', 'b']


'''Индексация элементов списков
Узнать индекс заданного элемента списка x можно с помощью метода list.index(x):'''
print([2, 2, 4].index(2))
# 0
print([2, 2, 4].index(2,1))
# 1
'''Метод index(x) ищет первое вхождение элемента x в списке и возвращает его индекс. Как и другие основные языки программирования, Python присваивает индекс 0 первому элементу, а индекс i – 1 — i-му элементу.'''

                                                   # 33 множества (кортежи)

hero = "Harry"
guide = "Dumbledore"
enemy = "Lord V."
print(hash(hero))
# 6175908009919104006
print(hash(guide))
# -5197671124693729851
## Можно ли создать множество строковых значений?
characters = {hero, guide, enemy}
print(characters)
# {'Lord V.', 'Dumbledore', 'Harry'}
characters = {hero, guide, enemy}
print(characters)
clone_army = {hero, hero, hero, hero, hero, enemy}
print(clone_army)
# {'Lord V.', 'Harry'}

                                            # словари

calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}
'''Читать и записывать элементы можно путем указания ключа в квадратных скобках:'''
print(calories['apple'] < calories['choco'])
# True
calories['cappu'] = 74
print(calories['banana'] < calories['cappu'])
# False
'''Для доступа ко всем ключам и значениям ассоциативного массива служат функции keys() и values() соответственно:'''
print('apple' in calories.keys())
# True
print(52 in calories.values())
# True
'''Для доступа к парам (ключ, значение) ассоциативного массива служит метод items():'''
for k, v in calories.items():
 print(k) if v > 500 else None
# 'choco'

                                  # Ключевое слово in
print(42 in [2, 39, 42])
# True
print("21" in {"2", "39", "42"})
# False
print("list" in {"list" : [1, 2, 3], "set" : {1,2,3}})
# True

                           # Списковые включения и включения множеств

# (имя, $-доход)
customers = [("John", 240000),
("Alice", 120000),
("Ann", 1100000),
("Zach", 44000)]
# Ценные клиенты, зарабатывающие более $1 млн
whales = [x for x,y in customers if y>1000000]
print(whales)
# ['Ann']


                                             # 41 


 # lambda лямбда 
''' map() — это встроенная функция Python, принимающая в качестве аргумента функцию и последовательность. Она работает так, что применяет переданную функцию к каждому элементу.'''
L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))
# [1, 4, 9, 16]

''' filter() — это еще одна встроенная функция, которая фильтрует последовательность итерируемого объекта.

Другими словами, функция filter отфильтровывает некоторые элементы итерируемого объекта (например, списка) на основе какого-то критерия. Критерий определяется за счет передачи функции в качестве аргумента. Она же применяется к каждому элементу объекта.'''

def even_fn(x):
  if x % 2 == 0:
    return True
  return False

print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))

#вывод: [2, 20]

# то же самое в одну строку
print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))

'''Лямбда-функция и сортировка списков
Сортировка списка — базовая операция в Python. Если речь идет о списке чисел или строк, то процесс максимально простой. Подойдут встроенные функции sort и sorted.

Но иногда имеется список кастомных объектов, сортировать которые нужно на основе значений одного из полей. В таком случае можно передать параметр key в sort или sorted. Он и будет являться функцией.

Функция применяется ко всем элементам объекта, а возвращаемое значение — то, на основе чего выполнится сортировка. Рассмотрим пример. Есть класс Employee.'''

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
'''Теперь создадим экземпляры этого класса и добавим их в список.'''

Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]
'''Предположим, что мы хотим отсортировать его на основе поля age сотрудников. Вот что нужно сделать для этого:
'''
L.sort(key=lambda x: x.age)
print([item.name for item in L])
# вывод: ['David', 'Alex', 'Amanda']
'''Лямбда-выражение было использовано в качестве параметра key вместо отдельного ее определения и затем передачи в функцию sort.'''


def even_fn(x):
  if x % 2 == 0:
    return True
  return False

print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))


                                       # 41


employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}
top_earners = []
for key, val in employees.items():
 if val >= 100000:
  top_earners.append((key,val))
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]

print([(key,val) for key, val in employees.items() if val >= 100000])

print('------------')

print([(x, y) for x in range(3) for y in range(3)])
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print('------------')


                                           # 44


print([x ** 2 for x in range(10) if x % 2 > 0])
# [1, 9, 25, 49, 81]

'''Выражение : функция возведения в квадрат переменной контекста x.
Контекст : переменная контекста x проходит в цикле по всем значениям, возвращаемым функцией range — 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, — но только нечетным, то есть когда x % 2 > 0.'''

print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])
# ['i', 'am', 'not', 'shouting']

'''Выражение : строковая функция приведения к нижнему регистру переменной контекста x.
Контекст : переменная контекста x проходит в цикле по всем строковым значениям в списке: 'I', 'AM', 'NOT', 'SHOUTING'.'''


                                          # 45

employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}

top_earners = [(k, v) for k, v in employees.items() if v >= 100000]

# Поиск информативных слов с помощью спискового включения

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
## Однострочник
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]
## Результат
print(w)

'''Чтение файла
В этом разделе мы прочитаем данные из файла и сохраним результат в виде списка строковых значений (по одному на строку). Мы также удалим из прочитанных строк все ведущие и хвостовые пробельные символы.'''

filename = "readFileDefault.py" # этот код
f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
print(lines)

print([line.strip() for line in open("readFileDefault.py")])

                                          # 51

'''Однострочное решение, помечающее строковые значения, содержащие строку символов 'anonymous''''
## Данные
txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']
## Однострочник
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
## Результаты
print(list(mark))

                                            # 55

'''Листинг 2.5. Однострочное решение для поиска в тексте последовательностей символов и их непосредственного окружения'''
## Данные
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
## Однострочник
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
## Результат
print(find(letters_amazon, 'SQL'))

'''Код
Наша цель — заменить каждое второе строковое значение на непосредственно предшествующее ему (листинг 2.7).
Листинг 2.7. Однострочное решение для замены всех испорченных строк'''
## Данные
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
'Safari', 'corrupted', 'Safari', 'corrupted',
'Chrome', 'corrupted', 'Firefox', 'corrupted']
## Однострочник
visitors[1::2] = visitors[::2]
## Результат
print(visitors)

                                           # 62

# Зависимости
import matplotlib.pyplot as plt
## Данные
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
## Однострочник
expected_cycles = cardiac_cycle[1:-2] * 10
## Результат
plt.plot(expected_cycles)
plt.show()

                                            # 65

'''вместо вычисления квадратов первых 20 натуральных чисел с помощью спискового включения, sum([x*x for x in range(20)]), можно воспользоваться выражением-генератором: sum(x*x for x in range(20))'''
print(sum([x*x for x in range(20)]))
print(sum(x*x for x in range(20)))

'''Наши данные представляют собой ассоциативный массив ассоциативных массивов, в которых хранятся почасовые ставки работников компаний. Необходимо выделить из него список компаний, платящих по крайней мере одному сотруднику меньше установленной законом минимальной почасовой ставки (< $9) (листинг 2.9).
Листинг 2.9. Однострочное решение для поиска компаний, платящих меньше установленной законом минимальной почасовой ставки'''

## Данные
companies = {
'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
## Однострочник
illegal = [x for x in companies if any(y<9 for y in companies[x].values())]
## Результат
print(illegal)

                                           # 66

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
# Упаковка двух списков вместе
zipped = list(zip(lst_1, lst_2))
print(zipped)
# [(1, 4), (2, 5), (3, 6)]
# Обратная распаковка списков
lst_1_new, lst_2_new = zip(*zipped)
print(list(lst_1_new))
print(list(lst_2_new))

'''Функция zip() принимает на входе итерируемые объекты iter_1, iter_2, ..., iter_n и агрегирует их в один итерируемый объект путем выстраивания соответствующих i-х значений в один кортеж. В результате получается итерируемый объект из кортежей. Например, рассмотрим следующие два списка:
Оператор * служит для распаковки  всех элементов списка. Этот оператор удаляет внешние квадратные скобки списка zipped'''


                                           ### 68


'''У вас есть база данных всех сотрудников с названиями столбцов 'name', 'salary' и 'job'. Однако ваши данные не маркированы, они представляют собой просто набор строк вида ('Bob', 99000, 'mid-level manager'). Необходимо связать эти названия столбцов с элементами данных и привести их в удобочитаемый вид: {'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'}. Как это сделать?'''

## Данные
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
('Bob', 99000, 'mid-level manager'),
('Frank', 87000, 'CEO')]
## Однострочник
db = [dict(zip(column_names, row)) for row in db_rows]
## Результат
print(db)

                                        # 72

'''В листинге 3.2 приведены примеры простейших арифметических операций над двумерными массивами.
Листинг 3.2. Простейшие арифметические операции с массивами'''
import numpy as np
# Создание одномерного массива из списка
a = np.array([1, 2, 3])
print(a)
"""
[1 2 3]
"""
# Создание двумерного массива из списка списков
b = np.array([[1, 2],
[3, 4]])
print(b)
"""
[[1 2]
[3 4]]
"""
# Создание трехмерного массива из списка списков списков
c = np.array([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print(c)
"""
[[[1 2]
[3 4]]
[[5 6]
[7 8]]]
"""

                                         # 75

'''Листинг 3.3. Вычисление максимального, минимального и среднего значений массива NumPy
import numpy as np'''
a = np.array([[1, 0, 0],
[1, 1, 1],
[2, 0, 0]])
print(np.max(a))
# 2
print(np.min(a))
# 0
print(np.average(a))
# 0.6666666666666666

