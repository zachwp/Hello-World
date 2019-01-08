'''Identifies voodoo primes.

   A voodoo prime is a prime number that occurs within its reciprocal value.'''

def f():
    x = int(input("Enter a whole number: "))
    y = 1 / x
    for i in range(2, x):
        if x % i == 0 and i != x:
            print('not prime')
            print(1 / x)
            f()
        
    else:
        print('prime')
        print(1 / x)
        print(str(y))
        print(str(x))
        if str(x) in str(y):
            print('Is also a voodoo prime')
            f()
        f()
        

print(__doc__)
f()
