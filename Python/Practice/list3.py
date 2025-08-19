name = 'TejasPundpal'

print(min(name))
print(max(name))

list1 = [x**2 for x in range(1,11)]
print(list1)
list2 = [x for x in range(1,11) if x % 2 == 0]
print(list2)
list3 = [(x, x**2) for x in range(1,11)]
print(list3)
list4 = [x**2 if x % 2 == 0 else x for x in range(1,11)]
print(list4)
list5 = [(x,y) for x in range(1,4) for y in range(1,4) if y > x ]
print(list5)