if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        
    sub_arr = []   
    for i in range(len(arr)):
        if arr[i][1] not in sub_arr:
            sub_arr.append(arr[i][1])
    
    sub_arr.sort()        
    # for i in range(len(sub_arr)-1):
    #     if sub_arr[i]>sub_arr[i+1]:
    #         temp = sub_arr[i]
    #         sub_arr[i+1] = sub_arr[i]
    #         sub_arr[i] = temp
    
    num = sub_arr[1]
    
    final_list = []
    for i in range(len(arr)):
        if arr[i][1] == num:
            final_list.append(arr[i][0])
            
    final_list.sort()
    for i in final_list:
        print(i)        
            