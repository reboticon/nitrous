numbers = input()
for n in numbers:
    a, b = numbers.split()
    print(int(a) + int(b), end=' ')
    numbers = input()