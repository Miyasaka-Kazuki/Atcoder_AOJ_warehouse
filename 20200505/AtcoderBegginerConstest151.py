# ・D - Maze Master
#appendを使ったバージョン
H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]

def update(y, x, direction, d, q):
    next_y, next_x = (y + direction[0], x + direction[1])
    if (next_y < 0 or next_y >= H or next_x < 0 or next_x >= W): # 端なら
        return
    if (S[next_y][next_x] == '#') or (d[next_y][next_x] != -1): # 壁か既に訪問状態なら
        return
    d[next_y][next_x] = d[y][x] + 1
    q.append((next_y, next_x))

def bfs(i, j):
    DIJ = ((-1, 0), (0, -1), (1, 0), (0, 1)) # (y, x):下, 左, 上, 右
    dist = [[-1] * W for _ in range(H)]
    dist[i][j] = 0 #始点は０

    queue = [(i, j)]
    while queue:
        cur_y, cur_x = queue.pop(0)
        for i in range(4):
            update(cur_y, cur_x, DIJ[i], dist, queue)
    return max(max(dd) for dd in dist)

max_results = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            max_results = max(bfs(i, j), max_results)
print(max_results)


#appendを使わないバージョン
H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]

def update(y, x, direction, d, q, end_pos):
    next_y, next_x = (y + direction[0], x + direction[1])
    if (next_y < 0 or next_y >= H or next_x < 0 or next_x >= W): # 端なら
        return end_pos
    if (S[next_y][next_x] == '#') or (d[next_y][next_x] != -1): # 壁か既に訪問状態なら
        return end_pos
    d[next_y][next_x] = d[y][x] + 1
    q[end_pos] = (next_y, next_x)
    return end_pos + 1

def bfs(i, j):
    DIJ = ((-1, 0), (0, -1), (1, 0), (0, 1)) # (y, x):下, 左, 上, 右
    dist = [[-1] * W for _ in range(H)]
    dist[i][j] = 0 #始点は０

    wall_num = sum(ss.count('#') for ss in S)
    queue = [(-1, -1) for _ in range(H * W - wall_num)]
    queue[0] = (i, j)
    queue_end_pos = 1 # 一番後ろの値の+1
    while queue:
        cur_y, cur_x = queue.pop(0)
        queue_end_pos -= 1
        for i in range(4):
            queue_end_pos =             update(cur_y, cur_x, DIJ[i], dist, queue, queue_end_pos)
    return max(max(dd) for dd in dist)

max_results = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            max_results = max(bfs(i, j), max_results)
print(max_results)
