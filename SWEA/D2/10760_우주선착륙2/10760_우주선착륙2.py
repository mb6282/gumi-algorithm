T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    direction = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx or dy]
    total = 0

    for x in range(N):
        for y in range(M):
            count = 0
            for dx, dy in direction:
                check_x = x + dx
                check_y = y + dy
                if 0 <= check_x < N and 0 <= check_y < M:
                    if matrix[x][y] > matrix[check_x][check_y]:
                        count += 1
            if count >= 4:
                total += 1

    print(f'#{tc+1} {total}')