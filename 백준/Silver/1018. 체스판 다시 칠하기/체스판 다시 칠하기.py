n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

wb = []
bw = []
for _ in range(4):
    wb.append(list('WB' * 4))
    wb.append(list('BW' * 4))

    bw.append(list('BW' * 4))
    bw.append(list('WB' * 4))


answer =[]
for a in range(0, n-7):
    for b in range(0, m-7):
        bc = 0
        wc = 0
        for i in range(8):
            for j in range(8):
                # print((a, b), (a+i, b+j))
                if board[a+i][b+j] != wb[i][j]:
                    wc += 1
                if board[a+i][b+j] != bw[i][j]:
                    bc += 1
        answer.append(min(wc, bc))
        
print(min(answer))