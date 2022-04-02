n = int(input())
rope = []
val = []

for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
for num in range(n):
    val.append(rope[num]*(num+1))
print(max(val))