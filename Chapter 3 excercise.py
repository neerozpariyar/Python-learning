h = input('Enter hours: ')
r = input('Enter rate: ')
hours = float(h)
rate = float(r)
if hours>40:
    reg = hours*rate
    otp = (hours - 40) * (rate * 0.5)
    pay = reg + otp
else:
    pay = hours * rate
print('Pay:',pay)

#using tru and catch

h = input('Enter hours: ')
r = input('Enter rate: ')
try:
    hours = float(h)
    rate = float(r)
except:
    print('Enter a numeric type value')
    exit()
   
if hours>40:
    reg = hours*rate
    otp = (hours - 40) * (rate * 0.5)
    pay = reg + otp
else:
    pay = hours * rate
print('Pay:',pay)




