t = int(input())
for i in range(t):
    data1 = input()
    data = input()
    data2 =data.split()
    n,x = map(int,data1.split())
    doors = list(map(int,data2))
    flag = True
    for i in range(n):
        if doors[i]==1:
            for j in range(i+x,n):
                if doors[j] == 1:
                    flag = False
                    break
            break
    
                    
    if flag:
        print('YES')
    else:
        print('NO')
#

    