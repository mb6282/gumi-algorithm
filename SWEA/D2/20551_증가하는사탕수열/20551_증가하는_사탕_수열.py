T = int(input())
for trial in range(1, T+1):
    a, b, c = map(int, input().split())

    candy = 0
    while not(a<b<c): # 감소 수 최소화
        if c < 3 or b < 2:
            candy = -1
            break
        elif b >= c:
            candy += b-c+1
            b = c-1
            if a >= b:
                candy += b-a+1
                a = b-1
                continue # 값 바꿨으니 다시 검사
        elif b < c:
            if a >= b:
                candy += a-b+1
                break

    print(f'#{trial} {candy}')