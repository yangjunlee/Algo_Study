import bisect

n = int(input())
nums = list(map(int,input().split()))
dp = [0]*(n)

dp2 = [-float('inf')]

for i in range(n):
    if nums[i] > dp2[-1]:
        dp2.append(nums[i])
        dp[i] = len(dp2)-1
    else:
        dp[i] = bisect.bisect_left(dp2,nums[i])
        dp2[dp[i]] = nums[i]
print(len(dp2)-1)

max_idx,ans = max(dp),[]
for i in range(n-1,-1,-1):
    if dp[i] == max_idx:
        ans.append(nums[i])
        max_idx = dp[i]-1
print(*ans[::-1])
