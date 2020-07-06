# length of fib series for the max value <= x
print('{:<15} {:>10} {:>20}'.format('Below', 'Length', 'Series'))
for x in [10, 100, 1000, 10000, 100000, 1000000, 10000000, \
          100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000]:
    a, b = 0, 1
    f = []
    f.append(a)
    while b < x:
        f.append(b)
        a, b = b, a+b
    print(f'{x:<15} {len(f):<10} Series: {f}')
    #print(f'{len(f):<10}')
