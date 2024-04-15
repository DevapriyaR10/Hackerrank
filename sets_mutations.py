n = int(input())
a = set(map(int, input().split()))
m = int(input())

for i in range(m):
    com = input().split()
    if com[0] == "intersection_update":
        b = set(map(int, input().split()))
        a.intersection_update(b)

    elif com[0] == "difference_update":
        c = set(map(int, input().split()))
        a.difference_update(c)

    elif com[0] == "symmetric_difference_update":
        d = set(map(int, input().split()))
        a.symmetric_difference_update(d)

    elif com[0] == "update":
        e = set(map(int, input().split()))
        a.update(e)

total = sum(a)
print(total)
