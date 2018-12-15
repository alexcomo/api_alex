string = 'kabcbfdgblhbalajbjckjsndcfcfba'
sub = 'abc'


def sfind(string,sub):
    d = {}
    for i in sub:
        d[i] = 0

    while string:
        for s in range(len(string)):
            if cehck_dict(d):
                print(cehck_dict(d))
                for k, v in d.items():
                    if string[s] == k:
                        d[k] = s

                        break
                print(d)
            else:
                for k, v in d.items():
                    d[k] = 0
                #print(d)
                break
    return d

def cehck_dict(d):
    for k, v in d.items():
        if v == 0:
            return True
    return False


# def permutation(lst):
#     for i in lst:
#     privius = sub[0]
# if string[s] == privius:
#     d[privius] = s
# print(privius)
#
# def sfind(string,sub):
#     d={}
#     for i in sub:
#         d[i] = []
#     for i in sub:
#         for s in range(len(string)):
#             if string[s] == i:
#                 d[i].append(s)
#     print(d)
#     tmp = []
#     for k, v in d.items():
#         tmp.append(v)
#     print(tmp)
#     lst = []
#     for i in tmp:
#         for k in i:
#             lst.append([k])
#
#     l = permutation(lst)
#     print(l)
#     for i in list(l):
#         if max(i) - min(i) < tmp:
#             tmp = max(i) - min(i)
#             result = [min(i), max(i)]
#     print(result)
#     print(string[result[0]:result[1]])

#    for i in range(tmp):



print(sfind(string,sub))





# def sfind(string,sub):
#     dd = []
#     while len(string) > len(sub):
#         d = []
#         for s in sub:
#             for i in range(len(string)):
#                 if s == string[i]:
#                     d.append(i)
#                     break
#         min_in = min(d)
#         max_in = max(d)
#         dd.append(string[min_in: max_in+1])
#         string = string[max_in+1:]
#     return min(dd, key=len)
#
# print(sfind(string, sub))

# def get(s, alphabet="abc"):
#     seen = {}
#     for c in alphabet:
#         seen[c] = 0
#     seen[s[0]] = 1
#     start = 0
#     end = 0
#     shortest_s = 0
#     shortest_e = 99999
#     while end + 1 < len(s):
#         while seen[s[start]] > 1:
#             seen[s[start]] -= 1
#             start += 1
#         # Constant time check:
#         if sum(seen.values()) == len(alphabet) and all(v == 1 for v in seen.values()) and \
#                 shortest_e - shortest_s > end - start:
#             shortest_s = start
#             shortest_e = end
#         end += 1
#         seen[s[end]] += 1
#     return s[shortest_s: shortest_e + 1]
#
#
# print(get("abfbcac")) # Expected to return "bca"



