ar = 'Artyom'
s = 'Sergey'
ak = 'Akim'
m = 'Maksim'
v = 'Vladislav'
list_of_names = [ar, s, ak, m, v]
names = list_of_names
print('L:', names)
name_container = 'Artyom', 'Sergey', 'Akim', 'Maksim', 'Vladislav'
one, two, three, four, five = 'Artyom', 'Sergey', 'Akim', 'Maksim', 'Vladislav'
one, two = two, one
print('St1: ', one, two, three, four, five)
one = two = three = four = five = two
print(one, two, three, four, five)