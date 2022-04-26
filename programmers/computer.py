# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# len(computers)
#
# d = [0] * len(computers)
# d
#
# def dfs(graph, start):
#     going, visited = [], []
#     going.append(start)
#
#     while going:
#         node = going.pop()
#
#         if node not in visited:
#             visited.append(node)
#             going.extend(graph[node])


a = [1, 2, 3 ,5, 1]
a.count(1)
a.remove(1)
a
import numpy as np
np.mean(a)

a.remove(3)
a

np.mean([65, 77, 67, 65])