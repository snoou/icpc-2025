n, k = map(int, input().split())
a = list(map(int, input().split()))
happy = 0
for x in a:
    happy += x // k
print(happy)
