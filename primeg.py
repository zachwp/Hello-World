i = 2
primes = []
while i > 1:
    i += 1
    for n in range(2, i):
        if i % n == 0 and i != n:
            break
    else:
        primes.append(i)
        print(i)

