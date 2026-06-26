from collections import deque

t = int(input())

for _ in range(t):
    next_test = False
    n,a,b = map(int, input().split(' '))

    if a + b > n:
        print("NO")
        continue

    if a+b == 1:
        print("NO")
        continue

    
    player_b = list(range(1,n+1))
    player_a = []

    index = 0

    for card in range(b+1, b+a+1):
        player_a.append(card)

        if player_a[index] <= player_b[index]:
            print("NO")
            next_test = True
            break

        index += 1

    if next_test: continue

    for card in range(1, b+1):
        player_a.append(card)

        if player_a[index] >= player_b[index]:
            print("NO")
            next_test = True
            break

        index += 1

    if next_test: continue


    for card in range(a+b+1, n+1):
        player_a.append(card)

        if player_a[index] != player_b[index]:
            print("NO")
            next_test = True
            break

        index += 1

    if next_test: continue

    print("YES")
    print(*player_a)
    print(*player_b)
    # draws = n - a - b

    # A = [i for i in range(1, draws+1)]
    # B = [i for i in range(1, draws+1)]

    # A_available_cards = deque([j for j in range(draws+1, n+1)])

    # B_available_cards = A_available_cards.copy()

    # if a >= b:        
    #     for i in range(a):
    #         left = B_available_cards.popleft()
    #         B_available_cards.append(left)
    
    # else:
    #     for i in range(b):
    #         left = A_available_cards.popleft()
    #         A_available_cards.append(left)
    
        

    # A = A + list(A_available_cards)
    # B = B + list(B_available_cards)

    # print("YES")
    # print(*A)
    # print(*B)
    # for i in A.copy():
    #     if a == 0:
    #         break

    #     if i - 1 in B:
    #         res.add((i, i-1))
    #         A.remove(i)
    #         B.remove(i-1)
    #         a -= 1

    # for i in B.copy():
    #     if b == 0:
    #         break

    #     if i - 1 in A:
    #         res.add((i-1, i))
    #         A.remove(i-1)
    #         B.remove(i)
    #         b -= 1
