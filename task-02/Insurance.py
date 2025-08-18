t = int(input())
for i in range(t):
    data = input()
    data_l = data.split()
    a , b = map(int,data_l)
    if b >= a:
        print(a)
    else:
        print(b)