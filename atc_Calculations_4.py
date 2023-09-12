def solve(n, a):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(a)
    diff = expected_sum - actual_sum
    
    if diff == 0:
        print("Correct")
    else:
        duplicate = [False] * (n + 1)
        for num in a:
            if duplicate[num]:
                incorrect_num = num
                break
            duplicate[num] = True
        
        print(f"{incorrect_num} {incorrect_num + diff}")

# 入力を受け取る
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

# 問題を解く関数を呼び出す
solve(n, a)
