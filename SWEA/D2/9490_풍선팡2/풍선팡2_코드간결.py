T = int(input())
for case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    for row in range(N):
        for col in range(M):
            num = matrix[row][col]
            total_value = num

            if row - 1 >= 0:
                total_value += matrix[row - 1][col]

            if row + 1 < N:
                total_value += matrix[row + 1][col]

            if col - 1 >= 0:
                total_value += matrix[row][col - 1]

            if col + 1 < M:
                total_value += matrix[row][col + 1]

            if max < total_value:
                max = total_value

    print(f'#{case} {max}')