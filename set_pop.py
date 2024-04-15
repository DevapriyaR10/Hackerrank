n = int(input())
s = set(map(int, input().split()))
com = int(input())

for i in range(com):
    command = input().split()
    if command[0] == 'pop':
        if s:  # Check if set is not empty before trying to pop
            s.pop()
    elif command[0] == 'remove':
        if len(command) == 2:
            e = int(command[1])
            if e in s:
                s.remove(e)
    elif command[0] == 'discard':
        if len(command) == 2:
            h = int(command[1])
            s.discard(h)

# Calculate the sum of the elements in the set after each operation
result_sum = sum(s)
print(result_sum)
