t = int(input())

for i in range(t):
    dict1 = dict()
    N = input()
    data = input()
    datas = data.split()
    lst = list(map(int,datas))

    for i in lst:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] +=1
    greatest = 0
    
    for i in dict1:
        if dict1[i]>greatest:
            greatest = dict1[i]
    remove_card = 0
    count_max = 0
    for i in dict1:
        if dict1[i] != greatest:
            remove_card += dict1[i]
        else:
            count_max+=1

    remove_card += (count_max -1)*greatest
    print(remove_card)

