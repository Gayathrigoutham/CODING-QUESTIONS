def longest_substring_with_k_unique(s, k):
    start = 0
    max_len = 0
    freq = {}

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1

        while len(freq) > k:
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1

        if len(freq) == k:
            max_len = max(max_len, end - start + 1)

    return max_len

s = input()
k = int(input())
print(longest_substring_with_k_unique(s, k))
