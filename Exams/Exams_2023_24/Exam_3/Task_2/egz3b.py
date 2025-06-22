from egz3btesty import runtests


def kunlucky(T, k):
  n = len(T)
  i = 1
  unlucky = k
  memo = {}
  idx = []
  memo[k] = k
  memo[k+7] = k+7
  while unlucky <= n and i < n:
    unlucky = unlucky + (unlucky % i) + 7
    i += 1
    memo[unlucky] = unlucky
  for x in range(n):
    if T[x] in memo:
      idx.append(x)
  if len(idx) <= 2:
    return n
  result = [0] * len(idx)
  result[0] = idx[1]
  result[1] = idx[2]
  for x in range(2, len(idx)-1):
    result[x] = idx[x+1] - (idx[x-2]+1)
  result[len(idx)-1] = n-1 - idx[len(idx) - 3]
  return max(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )