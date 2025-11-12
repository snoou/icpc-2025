def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    if k == 2:
        pat1 = [1 if i % 2 == 0 else 2 for i in range(n)]
        pat2 = [2 if i % 2 == 0 else 1 for i in range(n)]
        diff1 = sum(A[i] != pat1[i] for i in range(n))
        diff2 = sum(A[i] != pat2[i] for i in range(n))
        if diff1 <= diff2:
            print(" ".join(map(str, pat1)))
        else:
            print(" ".join(map(str, pat2)))
        return

    B = A[:]
    for i in range(1, n):
        if B[i] == B[i - 1]:
            forbidden1 = B[i - 1]
            forbidden2 = A[i + 1] if i + 1 < n else -1
            for c in range(1, k + 1):
                if c != forbidden1 and c != forbidden2:
                    B[i] = c
                    break
    print(" ".join(map(str, B)))


if __name__ == "__main__":
    solve()
