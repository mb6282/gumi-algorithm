T = int(input())
for trial in range(1, T+1):
    a, b, c = map(int, input().split())
    candy = 0

    while not (a < b < c):
        # 불가능한 경우: C 최소 3, B 최소 2
        if c < 3 or b < 2:
            candy = -1
            break

        # B가 C보다 크거나 같으면 B를 C-1로 줄임
        if b >= c:
            after_b = c - 1
            candy += b - after_b
            b = after_b
            continue  # 값이 변했으니 다시 검사

        # A가 B보다 크거나 같으면 A를 B-1로 줄임
        if a >= b:
            after_a = b - 1
            candy += a - after_a
            a = after_a
            continue  # 값이 변했으니 다시 검사

        # 여기까지 오면 조건 만족
        break

    print(f'#{trial} {candy}')