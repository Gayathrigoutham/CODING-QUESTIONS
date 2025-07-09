 def group_anagrams():
    n = int(input())
    words = input().split()
    groups = {}

    for word in words:
        key = ''.join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    for group in groups.values():
        print(' '.join(group))