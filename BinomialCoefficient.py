# brute force 
def binomial_bf(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_bf(n-1, k-1) + binomial_bf(n-1, k)

# dynamicc programming
def binomial_dp(n, k):
    C = [[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

n, k = map(int, input("Enter n and k: ").split())
print("Brute Force:", binomial_bf(n, k))
print("DP:", binomial_dp(n, k))
