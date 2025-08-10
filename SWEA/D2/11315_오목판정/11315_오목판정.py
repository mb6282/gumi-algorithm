import sys
sys.stdin = open("sample_input.txt", "r")

def is_five(arr, N):
    d = [(0,1), (1,0), (1,1), (1,-1)] #오른쪽, 아래, \, /

    for x in range(N):
        for y in range(N):
            if arr[x][y] != '.': # 돌이 있는 경우에만 검사
                for dx, dy in d:
                    count = 1
                    nx, ny = x + dx, y + dy
                    # 중간이 돌이 없는 경우 방지를 위해 1씩 증가
                    while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o' :
                        count += 1
                        if count == 5:
                            return "YES"
                        nx += dx
                        ny += dy
    return "NO"

T = int(input())
for trial in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{trial} {is_five(arr, N)}')