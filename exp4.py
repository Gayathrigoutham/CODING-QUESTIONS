n = int(input())
nums = list(map(int, input().split()))
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing_number = expected_sum - actual_sum
print(missing_number)
