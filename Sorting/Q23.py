n = int(input())
student = []
for i in range(n):
    student.append(list(input().split()))

for i in student:
    for j in range(3):
        i[j+1] = int(i[j+1])


student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])