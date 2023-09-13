def main():
    numbers = list(map(int, input().split()))
    numbers.sort()
    result = numbers[-3]
    print(result)

if __name__ == "__main__":
    main()
