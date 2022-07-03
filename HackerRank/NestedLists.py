if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        a.append([input(), float(input())])
        
    a.sort(key = lambda x: x[1])
    subl = [i for i in a if i[1] != a[0][1]]
    subl2 = [i for i in subl if i[1] == subl[0][1]]
    subl2.sort()
    
    for i in subl2:
        print(i[0])
