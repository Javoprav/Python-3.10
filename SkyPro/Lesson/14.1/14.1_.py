'Магические методы __repr__, __str__, __len__ и __add__'

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        if isinstance(other, Employee):
          return self.pay + other.pay
        else:
          raise ValueError('Не правильный формат')

    def __len__(self):
        return len(self.fullname)


emp_1 = Employee('Ivan', 'Ivanov', 50000)
print(emp_1)
# <__main__.Employee object at 0x00000149FD28FBD0>

print(emp_1)
# Employee('Ivan', 'Ivanov', 50000)

emp_1 = Employee('Ivan', 'Ivanov', 50000)
print(emp_1)
#Ivan Ivanov - Ivan.Ivanov@email.com

emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1 + emp_2)
# 110000

emp_1 = Employee('Ivan', 'Ivanov', 50000)
print(len(emp_1))
# 11

' Магический метод __call__'

class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if isinstance(args[0], str):
          return args[0].strip(self.__chars)
        else:
          raise ValueError('Не правильный формат')
          

# инициализируем символом, который хотим удалять
st1 = StripChars('!')
print(st1('!Attention!'))
# TypeError: 'StripChars' object is not callable

st1 = StripChars('!')
st2 = StripChars('?')

print(st1('!Attention!'))
# Attention
print(st1('?Attention?'))
# ?Attention?
print(st2('?Attention?'))
# Attention

'Магические методы __iter__ и __next__'

class EvenRange:
    """Возвращает только четные числа"""
    def __init__(self, stop):
        if not isinstance(stop, int):
            raise ValueError('Число должно быть целым')
        if stop < 0:
            raise ValueError('Число должно быть не отрицательным')
        self.stop = stop

    def __iter__(self):
        self.current_value = -2
        return self

    def __next__(self):
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration

r = EvenRange(9)
print(list(r))
# [0, 2, 4, 6, 8]

for i in r:
   print(i)
# 0
# 2
# 4
# 6
# 8


'Магические методы __enter__ и __exit__'

class MyOpen:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()



with MyOpen('text.txt', 'r') as fp:
    print(fp.read())