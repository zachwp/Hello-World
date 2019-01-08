def f():
    ''' Prime identifier.

    Prompts for input and returns wether it is prime or not.'''
    x = int(input("Enter a whole number: "))
    for i in range(2, x):
        if x % i == 0 and i != x:
            print('not prime')
            f()
    else:
        print('prime')
        f()

print(f.__doc__)
f()
