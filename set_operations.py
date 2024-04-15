n = int(input())
s = set(map(int, input().split()))
com = int(input())

# Apply the commands
for _ in range(com):
    command = input().split()
    if command[0] == 'pop':
        if s:
            s.pop()
    elif command[0] == 'remove':
        element = int(command[1])
        if element in s:
            s.remove(element)
    elif command[0] == 'discard':
        element = int(command[1])
        s.discard(element)

# Calculate the sum of the elements in the set
result_sum = sum(s)
print(result_sum)
