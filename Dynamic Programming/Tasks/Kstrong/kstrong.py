def kstrong(T, k):
  n = len(T)
  dp = [[-float('inf') for _ in range(k+1)] for __ in range(n)]
  dp[0][0] = T[0]

  for i in range(1, k+1):
    dp[0][i] = 0
  
  result = max(dp[0])

  for i in range(1, n):
    for j in range(k+1):
      dp[i][j] = dp[i-1][j] + T[i]

      if j > 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1])

      if j == 0:
        dp[i][j] = max(dp[i][j], T[i])
      else:
        dp[i][j] = max(dp[i][j], 0)
    
    result = max(result, max(dp[i]))
  
  return result