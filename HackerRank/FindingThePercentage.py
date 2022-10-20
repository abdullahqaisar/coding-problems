if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for i in student_marks:
        if i == query_name:
            for j in range(3):
                sum = sum + student_marks[i][j]
    
    print("{:.2f}".format(sum/3))
