def maximize_happiness(N, A):
    max_happiness = 0
    
    # すべての社員を異なるグループに含める場合の好ましさを計算
    for i in range(N):
        for j in range(i + 1, N):
            max_happiness += A[i][j]
    
    # 各社員を1つずつ既存のグループに追加して、好ましさを計算
    for k in range(N):
        for i in range(N):
            for j in range(i + 1, N):
                if i != k and j != k:
                    # 社員kをグループiまたはグループjに追加して好ましさを計算
                    happiness_with_k = max_happiness - A[i][j] + A[i][k] + A[j][k]
                    max_happiness = max(max_happiness, happiness_with_k)
    
    return max_happiness

# 入力を受け取る
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# グループ分けの好ましさの最大値を計算
result = maximize_happiness(N, A)
print(result)

