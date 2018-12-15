string = "abcabcbb"
# for index, i in enumerate(s):
#     print(index, i)


def ls(s):
    l = 0
    t = ""
    for i in s:
        if i not in t:
            t += i
        else:
            if len(t) > l:
                l = len(t)
            t = i
    return l
print(ls(string))
