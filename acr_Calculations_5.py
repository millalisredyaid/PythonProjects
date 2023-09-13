def main():
    N, Q = map(int, input().split())
    follow = [[False] * (N + 1) for _ in range(N + 1)]
    
    for _ in range(Q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            a, b = op[1], op[2]
            follow[a][b] = True
        elif op[0] == 2:
            a = op[1]
            for i in range(1, N + 1):
                if follow[i][a]:
                    follow[a][i] = True
        else:
            a = op[1]
            for i in range(1, N + 1):
                if follow[a][i]:
                    for j in range(1, N + 1):
                        if follow[i][j] and j != a:
                            follow[a][j] = True
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if follow[i][j]:
                print("Y", end="")
            else:
                print("N", end="")
        print()

if __name__ == "__main__":
    main()
