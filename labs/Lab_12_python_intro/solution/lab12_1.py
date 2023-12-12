with open('input.txt', 'r') as file:
    N, M = map(int, file.readline().split())
    if not (1 <= N <= 50 and 1 <= M <= 50):
        print("Нужны числа от 1 до 50!! измените числа в входном файле и перезапустите код.")

    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(M):
            if i + 1 < N and j + 2 < M:
                dp[i+1][j+2] += dp[i][j]
            if i + 2 < N and j + 1 < M:
                dp[i+2][j+1] += dp[i][j]

    result = dp[N-1][M-1]
    print(result)