def bm_horspool(pattern, text):
    m, n = len(pattern), len(text)
    if m > n: return -1
    skip = {ch: m for ch in set(text)}
    for i in range(m-1):
        skip[pattern[i]] = m - i - 1
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += skip.get(text[i], m)
    return -1

text = "this is the string to search in"
pattern = "the"
idx = bm_horspool(pattern, text)
print("Found at index:", idx if idx != -1 else "Not found")
