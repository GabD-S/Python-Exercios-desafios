def solve():
    a = [input() for _ in range(10)]
    sm = 0

    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                if i == 0 or i == 9 or j == 0 or j == 9:
                    sm += 1
                elif i == 1 or i == 8 or j == 1 or j == 8:
                    sm += 2
                elif i == 2 or i == 7 or j == 2 or j == 7:
                    sm += 3
                elif i == 3 or i == 6 or j == 3 or j == 6:
                    sm += 4
                elif i == 4 or i == 5 or j == 4 or j == 5:
                    sm += 5
    print(sm)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
