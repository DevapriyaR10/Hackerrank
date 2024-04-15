n = int(input())
a = set(map(int, input().split())) 

m = int(input())
b = set(map(int, input().split()))  

symmetric_diff = sorted(a.symmetric_difference(b))
for num in symmetric_diff:
    print(num)
    
