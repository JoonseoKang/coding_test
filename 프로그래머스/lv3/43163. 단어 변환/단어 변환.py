from string import ascii_lowercase
from copy import deepcopy
from collections import deque

def solution(begin, target, words):
    answer = 0
    if target in words:
        alphabet_list = list(ascii_lowercase)
        visited = []
        queue = deque([(begin, 0)])
        # print(queue.popleft())
        # print(queue.popleft())
        # print(x, y)
        visited.append(begin)

        
        while queue:
            s, c = queue.popleft()

            if s == target:
                break

            s = list(s)

            for i in range(len(s)):
                tmp_s = deepcopy(s)
                for j in alphabet_list:
                    tmp_s[i] = j
                    new_word = ''.join(tmp_s)
                    if new_word in words and new_word not in visited:
                        queue.append((new_word, c + 1))

                        visited.append(new_word)
            


            
            for i in queue:
                if i[0] == target:
                    answer = i[1]
                    break
                    
        

    return answer