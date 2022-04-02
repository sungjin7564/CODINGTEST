n, k = map(int,input().split())
arr = []
a = 0

for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)
    a+=1

if k > len(arr):
    print(0)
else:
    print(arr[k-1])