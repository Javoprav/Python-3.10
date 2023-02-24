'''### Задача 1

Напишите функцию `get_unique_names(names)`, которая принимает список и возвращает уникальные элементы из него в виде списка.'''

def get_unique_names(names):
    names_set = set(names)
    return names_set

names = ["Yvor", "Wendell", "Hogan", "Sadella", "Yvor", "Sadella", "Hogan"]

unique_names = get_unique_names(names)

print(unique_names)

### Задача 2

'''Напишите функцию, которая печатает имена из списка словарей в таком формате:

Kingsley
Tobit
Pace
Andreas
Anthia
'''

users = [{
  "id": 1,
  "first_name": "Kingsley",
  "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
}, {
  "id": 2,
  "first_name": "Tobit",
  "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
}, {
  "id": 3,
  "first_name": "Pace",
  "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
}, {
  "id": 4,
  "first_name": "Andreas",
  "url": "https://ifeng.com/morbi/vestibulum/velit.png"
}, {
  "id": 5,
  "first_name": "Anthia",
  "url": "https://google.com/eu/orci.aspx"
}]

def get_names_from_user_list(names):
    list = []
    for name in names:
        list.append(name["first_name"])
    return [print(n) for n in list]

print(get_names_from_user_list(users))

'''### Задача 2.5
Напишите функцию `get_ids(users)`, которая возвращает id из списка словарей в таком формате:
[1,2,3,...]
# Вернет [1,2,3,4,5]
'''
users = [{
  "id": 1,
  "first_name": "Kingsley",
  "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
}, {
  "id": 2,
  "first_name": "Tobit",
  "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
}, {
  "id": 3,
  "first_name": "Pace",
  "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
}, {
  "id": 4,
  "first_name": "Andreas",
  "url": "https://ifeng.com/morbi/vestibulum/velit.png"
}, {
  "id": 5,
  "first_name": "Anthia",
  "url": "https://google.com/eu/orci.aspx"
}]

def get_ids(users):
    list = []
    for name in names:
        list.append(name["id"])
    return list

print(get_ids(users))

'''### Задача 3
Напишите функцию `filter_yellow_only(animals)`, которая выводит только тех животных, которые желтые (yellow)
Пример вывода:
Francolinus coqui is Yellow
Petaurus norfolcensis is Yellow'''

animals = [{
  "id": 1,
  "specie": "Francolinus coqui",
  "color": "Yellow"
}, {
  "id": 2,
  "specie": "Petaurus norfolcensis",
  "color": "Yellow"
}, {
  "id": 3,
  "specie": "Pseudoleistes virescens",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Sula dactylatra",
  "color": "Maroon"
}, {
  "id": 5,
  "specie": "Echimys chrysurus",
  "color": "Teal"
}]

def filter_yellow_only(animals):
    yellow_cat = {}
    for line in animals:
        if line["color"] == "Yellow":
            yellow_cat[line["specie"]] = "Yellow"
    return yellow_cat

yellow_only = filter_yellow_only(animals)


'''### Задача 4
Напишите функцию  `filter_violet_only(animals)`, которая возвращает в формате списка id только тех животных, которые фиолетовые (`violet`) 
Пример ввода:'''

animals = [{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 3,
  "specie": "Ephipplorhynchus senegalensis",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Pycnonotus barbatus",
  "color": "Indigo"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}, {
  "id": 6,
  "specie": "Hippotragus niger",
  "color": "Teal"
}, {
  "id": 7,
  "specie": "Redunca redunca",
  "color": "Turquoise"
}]

def filter_violet_only(animals):
    violet_list = []
    for i in animals:
        if i["color"] == "Violet":
            violet_list.append(i["id"])
    return violet_list

# Вернет [1, 2, 5]
print(filter_violet_only(animals))

'''### Задача 5
Напишите функцию  `filter_violet_only(animals)`, которая возвращает в формате списка **словари** только тех животных, которые фиолетовые (`violet`)
# Должна вернуть 
[{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}]
'''

animals = [{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 3,
  "specie": "Ephipplorhynchus senegalensis",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Pycnonotus barbatus",
  "color": "Indigo"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}, {
  "id": 6,
  "specie": "Hippotragus niger",
  "color": "Teal"
}, {
  "id": 7,
  "specie": "Redunca redunca",
  "color": "Turquoise"
}]

def filter_violet_only(animals):
    violet_only = []
    for i in animals:
        if i["color"] == "Violet":
            violet_only.append(i)

    return violet_only

print(filter_violet_only(animals))

'''### Задача 6
Напишите функцию  `get_names_sorted(animals)`, которая возвращает в формате списка строк **названия** всех животных отсортированных по алфавиту.
# Должна вернуть  
["Cygnus atratus", "Macaca fuscata", "Ursus arctos"]'''

animals = [{
  "specie": "Macaca fuscata",
  "color": "Khaki"
}, {
  "specie": "Cygnus atratus",
  "color": "Aquamarine"
}, {
  "specie": "Ursus arctos",
  "color": "Yellow"
}]

def get_names_sorted(animals):
    list = []
    for i in animals:
        list.append(i["specie"])
    list.sort()
    return list

'''my_languages.sort(reverse=True)
sort()'''
print(get_names_sorted(animals))

import requests

url_new = requests.get("https://www.jsonkeeper.com/b/NPMT")
data = url_new.json()

def load_names(url):
    list_names = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            list_names.append(i["first_name"])
    return list_names

print(data[1])

'''### Задача 8

На внешнем сервере хранится список со вложенным словарем. Напишите функцию `load_names(url)`, которая превратит его в список вида:
[”Имя”, “Имя”, “Имя”, ”Имя”]
'''
import requests as requests
import json

URL = "https://jsonkeeper.com/b/NPMT"

def load_names(url):
    req = requests.get(url)
    data = req.json()
    list_names = []  #list_names = set()
    
    for i in data:
        list_names.append(i["first_name"])  #list_names.add(i["first_name"])
    return list_names   #return list(list_names)
    #names = set(i["first_name"] for i in data)

print(load_names(URL))