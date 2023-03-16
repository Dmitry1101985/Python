# x, y, z = 1, 4, 5
# cortej = 1, 5, 7, 9, 15 #tuple
# print(type(cortej))
# # unpack tuple
# a, b, c, d, e = cortej
# print(a, b, c, d, e)
# print(cortej)
# *first, x = cortej #first - new tuple; x - last element
# f, g, *last = cortej #last - new tuple
# print(first)
# print(last)
# print(*cortej)

# def hello(name:str, n:int):
#     for i in range(n):
#         print(f'Hello {name}')


# name = input('What is your name?  ')
# n = int(input('How many times print?  '))

# hello(name, n)
# new_cortej = 'Dmytro', 7 #it is tuple
# hello(*new_cortej)

# цикл for перебирає ітеруємі об'єкти
# є два варіанти запису циклу:

# for x in range(start, stop, step):
#     do something
    
# for x in range(start, stop):
#     do something
    
# for x in range(object):
#     do something

# A = 22, 12, 3, 10, 25

# for x in A:
#     print(x)
    
# tuple (кортежі) незмінні, списки(масиви) - змінні

# tuple1 = 10, 20
# tuple2 = 10, 30
# tuple3 = 10, 40
# tuple4 = 10, 50
# tuple5 = 10, 60
# tuple6 = 10, 70
# tuple7 = 10, 80

# list_a = [tuple1, tuple2, tuple3, tuple4, tuple5, tuple6]
# list_a.append = tuple7

# # for x in range(len(list_a)):
# #     do something

# import turtle

# # for tup in list_a:
# #     angle, length = tup
# #     turtle.forward(length)
# #     turtle.left(angle)

# for angle, length in list_a:
#     turtle.forward(length)
#     turtle.left(angle)
    
# Множини (set) і словники(dict) 
# дані в них не упорядковані
# в множині не можуть дублюватися дані

# a_set = {'Kyiv', 'Kharkiv', 'Odesa', 'Brovary', 'Chernigiv'}
# a_set.add ('Kherson')

# if 'Kherson' in a_set:
#     print(True)
# else:
#     print(False)
    
# for city in a_set:
#     print(city)
    
# словники - це множини, в яких зберігаються кортежи ключ-значення

a_dict = {'Kyiv': 10, 
          'Kharkiv': 20, 
          'Odesa': 30, 
          'Brovary' : 40, 
          'Chernigiv': 50}
a_dict['Kherson'] = 60

for key in a_dict:
    print(key, a_dict[key])
    
if 'Kherson' in a_dict:
    print(True)