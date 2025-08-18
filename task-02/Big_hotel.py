def modulus(x,y):
    if x>=y:
        result = x-y
    else:
        result = y-x
    return result
def find_floor(x):
    cnt = 0
    for i in range(1,11):
        if 10*(i-1)+1 <= x and   x <=(10*i):
            cnt+=i
    return cnt
t = int(input())
for i in range(t):
    data = input()
    datas = data.split()
    x,y = map(int,datas)
    print(modulus(find_floor(x),find_floor(y)))
    
        