n, m = map(int,input().split())

point = list(map(int, input().split()))

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

here = point[:2]
where = point[-1]

dx = [0, 1, 0, -1] #북 동 남 서
dy = [-1, 0, 1, 0]

import numpy as np
visted = np.zeros((4,4))

visted[here[0], here[1]] = 1

new = [0, 0]

d = [[0] * m for _ in range(n)]

