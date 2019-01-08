f = input('Enter a phone number area code included: ')
    
if len(f) == 10:
    print(f[:3] + '-' + f[3:6] + '-' + f[6:])
else:
    print('invalid try again')


