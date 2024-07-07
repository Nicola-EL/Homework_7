# Словари
my_dict = {'Valera':1978, 'Ulia':1990, 'Nikita':1995}
print(my_dict)
print(my_dict['Ulia'])
print(my_dict.get('Macha'))
my_dict.update({'Vary':1992, 'Vasy':2000})
print(my_dict)
del my_dict['Vary']
print(my_dict)
# Множества
my_set = {1,1,1,3,3,3,5,5,5}
print(my_set)
print(my_set.add(7))
print(my_set.add(9))
print(my_set)
print(my_set.discard(1))
print(my_set)
