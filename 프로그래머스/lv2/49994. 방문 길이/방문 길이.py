def solution(dirs):
    answer = set()
    d = {"U": [1, 0], "D": [-1, 0], "R": [0, 1], "L": [0, -1]}
    x, y = 0, 0
    
    for i in dirs:
        dx, dy = d[i]
        
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
            
    return len(answer) // 2