def maximize_happiness(N, A):
    max_happiness = 0
    
    for mask in range(1, 2**N):
        group_happiness = 0
        group_count = 0
        
        for i in range(N):
            if (mask >> i) & 1:  # 社員 i がグループに含まれる場合
                group_count += 1
                
                for j in range(i + 1, N):
                    if (mask >> j) & 1:  # 社員 j がグループに含まれる場合
                        group_happiness += A[i][j]
        
        if group_count <= 3:
            max_happiness = max(max_happiness, group_happiness)
    
    return max_happiness

# 入力を受け取る
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# グループ分けの好ましさの最大値を計算
result = maximize_happiness(N, A)
print(result)

