t = int(input())
for i in range(t):
    datas = input()
    data = datas.split()
    n,x,y = map(int,data)
    if (n+1)*y>=x:
        print('YES')
    else:
        print('NO')