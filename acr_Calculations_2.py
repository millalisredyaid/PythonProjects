def main():
    N = int(input())
    sales = [int(input()) for _ in range(N)]

    for i in range(1, N):
        diff = sales[i] - sales[i - 1]
        if diff == 0:
            print("stay")
        elif diff > 0:
            print("up", diff)
        else:
            print("down", -diff)

if __name__ == "__main__":
    main()
