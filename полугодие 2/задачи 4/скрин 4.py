def func(wasd):
    a=len(wasd)
    dp=[1]*a
    longest=1
    for i in range(1, a):
        for j in range(i):
            if wasd[j]>=wasd[i]:
                dp[i]=max(dp[i], 1 + dp[j])
        longest=max(longest, dp[i])
    return longest
print(func([5, 7, 2, 10, 6, 1, 3])) 