import math
import random

def greet():
    return 'Hello'


print(greet())


ratio = 9/10
decibles = 10*math.log10(ratio)
print(decibles)

degree = input('Enter a degree:')
degree = float(degree)
radian = degree / 180 * math.pi
height = math.sin(radian)
print(height) 


for i in range(2):
    x=random.random()
    print(x)

def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

def repeat_lyrics():
        print_lyrics()
        print_lyrics()



repeat_lyrics()