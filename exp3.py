from collections import Counter

def count_k_diff_pairs(arr, K):
    if K < 0:
        return 0

    pairs = set()

    if K == 0:
        freq = Counter(arr)
        for num in freq:
            if freq[num] > 1:
                pairs.add((num, num))
    else:
        nums = set(arr)
        for num in nums:
            if num + K in nums:
                pairs.add((num, num + K))

    for a, b in sorted(pairs):
        print(a, b)

    return len(pairs)

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

print(count_k_diff_pairs(arr, K))
