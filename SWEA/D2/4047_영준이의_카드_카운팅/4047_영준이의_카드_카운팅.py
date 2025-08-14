def card_vaild(card_lst):
    temp = []
    for card in card_lst :
        if card in temp: # 중복확인
            return "ERROR"
        else : 
            temp.append(card)
    if temp : # 카드 개수 차감
        for card in temp:
            perfect_card[card[0]] -= 1
            # Quiz : int(card[1:3])이 쓰이는 문제는 무엇일까요? # int 함수는 문자열을 정수로 바꿀 때 자동으로 앞의 0을 제거해줌
        return f'{perfect_card["S"]} {perfect_card["D"]} {perfect_card["H"]} {perfect_card["C"]}'
    else :
        return "ERROR"

T = int(input())
for trial in range(1, T + 1):
    case_str = input()
    card_lst = [case_str[i:i+3] for i in range(0, len(case_str), 3)]
    perfect_card = {suit: 13 for suit in 'SDHC'}
    print(f'#{trial} {card_vaild(card_lst)}')