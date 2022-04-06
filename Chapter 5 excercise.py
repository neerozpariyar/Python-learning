sums = 0.0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        print('Sum Total:',sums,'\nCount:',count,'\nAverage:',sums/count)
        break
    try:
        fval = float(inp)
    except:
        print('Invalid input')
        continue

    count = count + 1
    sums = sums + fval


        
 
    

