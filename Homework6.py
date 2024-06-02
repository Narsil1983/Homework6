my_dict = {'Sergey': 1983, 'Jura': 2000, 'Galina': 1960}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Anton'))
my_dict.update({'Evgeniy': 2002, 'Sasha': 1990})
print(my_dict)
a = my_dict.pop('Sergey')
print(a)

my_set_ = {1, 2, 3, 'Апельсин', 22.222, 1,2,3,'Апельсин', 22.222}
print(my_set_)
my_set_ = {1, 2, 3, 'Апельсин', 22.222, 1,2,3,'Апельсин', 22.222, (4,5, 45.225)}
print(my_set_)
list_ = [1, 2, 3, 'Апельсин', 22.222, 1,2,3,'Апельсин', 22.222, (4,5, 45.225)]
list_ = set(list_)
print(list_)
list_.discard(1)
print(list_)