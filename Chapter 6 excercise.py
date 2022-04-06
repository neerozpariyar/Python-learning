from lib2to3.pytree import LeafPattern


fruit = 'Banana'
index = (len(fruit)-1)

while (index)>=0:
    letter = fruit[index]
    print(letter)
    index = index-1
print('\n')

for char in fruit:
    print(char)