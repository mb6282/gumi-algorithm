T = int(input())
for case in range(1,T+1):
    # 값 설정
    N, M = list(map(int,input().split()))
    matrix = [ list(map(int,input().split())) for _ in range(N)]
    max = 0

    for row in range(N):
        for col in range(M):
            # 터트릴 풍선의 값
            num = matrix[row][col]
            total_value = num

            # 위쪽 터트리기
            # 위쪽으로만 연쇄적으로 터트리고 싶다면 range(1, row + 1)
            for up in range(1, 2):
                up_row = row - up
                if up_row < 0 :
                    break
                total_value += matrix[up_row][col]

            # 아래쪽 터트리기
            for down in range(1, 2):
                down_row = row + down
                if down_row >= N :
                    break
                total_value += matrix[down_row][col]

            # 왼쪽 터트리기
            for left in range(1, 2):
                left_col = col - left
                if left_col < 0 :
                    break
                total_value += matrix[row][left_col]

            # 오른쪽 터트리기
            for right in range(1, 2):
                right_col = col + right
                if right_col >= M :
                    break
                total_value += matrix[row][right_col]

            # 최대값 찾기
            if max < total_value :
                max = total_value
            
    print(f'#{case} {max}')

