if __name__ == '__main__':
    x = int(input("Enter a number"))
    y = int(input("Enter a number"))
    z = int(input("Enter a number"))
    n = int(input("Enter a number"))
 
    li = []
    i = 0

    while i <= x:
        j = 0
        while j <= y:
            k = 0
            while k <= z:
                if i + j + k != n:
                    li.append([i, j, k])
                k += 1
            j += 1
        i += 1

    print(li)
