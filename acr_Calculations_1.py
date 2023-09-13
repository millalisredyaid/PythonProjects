def main():
    S = input().strip()

    if S.isnumeric() and len(S) == 3:
        print(int(S) * 2)
    else:
        print("error")

if __name__ == "__main__":
    main()
