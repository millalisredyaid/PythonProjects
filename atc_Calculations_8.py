def main():
    N = int(input())  # カードの種類数を受け取る
    inventory = list(map(int, input().split()))  # カードの在庫数をリストとして受け取る
    Q = int(input())  # クエリの数を受け取る
    
    total_sold = 0  # 販売したカードの合計枚数を保持する変数
    
    for _ in range(Q):
        query = list(map(int, input().split()))  # クエリをリストとして受け取る
        
        if query[0] == 1:  # 単品販売の場合
            x, a = query[1], query[2]
            if inventory[x - 1] >= a:
                inventory[x - 1] -= a
                total_sold += a
        elif query[0] == 2:  # セット販売の場合
            a = query[1]
            for i in range(N):
                if (i + 1) % 2 == 1 and inventory[i] >= a:
                    inventory[i] -= a
                    total_sold += a
        else:  # 全種類販売の場合
            a = query[1]
            can_sell = True
            for i in range(N):
                if inventory[i] < a:
                    can_sell = False
                    break
            if can_sell:
                for i in range(N):
                    inventory[i] -= a
                total_sold += a * N
    
    print(total_sold)

if __name__ == "__main__":
    main()
