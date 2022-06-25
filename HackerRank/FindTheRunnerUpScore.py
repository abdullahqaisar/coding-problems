if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list = [-100, -100]
    for x in arr:
        if x > list[0]:
            temp = list[0]
            list[0] = x
            list[1] = temp
        elif x < list[0] and x > list[1]:
            list[1] = x
    print(list[1])
