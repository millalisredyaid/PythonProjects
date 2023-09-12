def main():
    numbers = list(map(int, input().split()))  # 6つの整数を受け取る
    numbers.sort()  # 数字を昇順にソート
    result = numbers[-3]  # 3番目に大きい数を取得
    print(result)

if __name__ == "__main__":
    main()
