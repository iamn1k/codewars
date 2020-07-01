def generate_hashtag(s):
    s = s.title()
    if len(s) > 140:
        return False
    if len(s) == 1 or len(s) == 0:
        return False
    res = ''
    for i in range(len(s)):
        if s[i] != ' ':
            res += s[i]
    return '#' + res