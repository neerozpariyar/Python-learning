n = 5
while n>0:
    print(n)
    n=n-1
print('Done')


while True:
    line = input('>>>')
    if line == 'done':
        break
    print(line)
print('Fuck off now')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')



count = 0

for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print(itervar,count)


total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)

#to print the largest number
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

