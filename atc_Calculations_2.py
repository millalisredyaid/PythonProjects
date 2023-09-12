def main():
    N = int(input())  # 日数を受け取る
    sales = [int(input()) for _ in range(N)]  # 売上データを受け取る

    for i in range(1, N):
        diff = sales[i] - sales[i - 1]  # 売上の差分を計算
        if diff == 0:
            print("stay")
        elif diff > 0:
            print("up", diff)
        else:
            print("down", -diff)

if __name__ == "__main__":
    main()
