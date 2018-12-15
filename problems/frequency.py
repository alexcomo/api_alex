# text = "alex max jon max"
#
#
# def count_words(text):
#
#     d = {}
#     l = text.split()
#     for i in l:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#
#     for keys, values in d.items():
#         print(keys + " : " + str(values))
#
# count_words(text)
text = "alex jon alex max"


def count_words(text):
    temp = text.split(" ")

    result = []
    count = []

    for item in temp:
        if item not in result:
            result.append(item)
            # print(result.index(item))

            count.append(0)

        count[result.index(item)] = count[result.index(item)] + 1

    for item in result:
        print("{0} : {1}".format(item, count[result.index(item)]))
count_words(text)