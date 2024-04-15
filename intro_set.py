def average(array):
    s=set(array)
    average_=(sum(s)/len(s))
    return average_
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)