


l=[2, 3, 4, 1, 4, 5]


def sum_m(l):
    left_sum = 0
    right_sum = sum(l)
    for i in range(len(l)):
        right_sum -= l[i]
        if left_sum == right_sum:
            return i
        left_sum += l[i]


# def sum_m(l):
#     tmp1 = 0
#     tmp2 = 0
#    # print(int(len(l)/2))
#     for i in range(int(len(l)/2)):
#         tmp1 += l[i]
#         tmp2 += l[i-i-1]
#         print(tmp1, tmp2)
#
print(sum_m(l))
