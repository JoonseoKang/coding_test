# https://www.acmicpc.net/problem/10162

"""
버튼A: 5분 = 300초
버튼B: 1분 = 60초
버튼C: 10초
"""

t = int(input())

time = [300, 60, 10]
press = [0, 0 ,0]


for i in range(len(time)):
    if t % 10 == 0 :
        press[i] += t // time[i]
        t -= time[i] * (t//time[i])
    else:
        press = -1

if press != -1:
    print(press[0], press[1], press[2])
else:
    print(press)