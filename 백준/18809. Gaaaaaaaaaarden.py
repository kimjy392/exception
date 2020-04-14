N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
lands = []

for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            lands.append((i, j))

# 심을 수 있는 곳에서 초록색을 우선 뽑고, 나머지 곳에서 빨간색을 뽑는다.
# 그리고 시뮬레이션을 진행