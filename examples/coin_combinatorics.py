MOD = 10**9 + 7
n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for x in range(1, 7):
        if i - x >= 0:
            dp[i] = (dp[i] + dp[i - x]) % MOD

# print(dp[n])

#
# rabbit = "Rabbit of Caerbannog",
# rabbbit2 = 34
# print(type(rabbbit2).__name__)


import functools

def thrush(x, y): return y(x)

def add_5(x): return x + 5
def minus_10(x): return x - 10
def mul_2(x): return x*2

pipeline = [2, add_5, minus_10, mul_2]
print(functools.reduce(thrush, pipeline))
