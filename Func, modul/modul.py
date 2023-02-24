import struct

for i in (4, 3, 2, 1, 0, -1, -2, -3, -4):
  byte = struct.pack('b', i)[0]
  print (f'{i} = {byte:08b}')

from decimal import Decimal

print(Decimal(0.2) + Decimal(0.1))

for i in "PYTHON":
  print(f'{i} = {ord(i)}, {bin(ord(i))}')