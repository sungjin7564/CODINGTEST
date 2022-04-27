n = int(input())
a = 1000 - n
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)