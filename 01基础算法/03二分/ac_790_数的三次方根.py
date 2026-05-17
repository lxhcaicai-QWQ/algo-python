
def main() -> None:
    n = float(input())
    l, r = -50.0, 50.0
    while abs(r - l) > 1e-8:
        mid = (l + r) / 2
        if mid ** 3 >= n:
            r = mid
        else:
            l = mid
    print(f"{r:.6f}")

if __name__ == "__main__":
    main()