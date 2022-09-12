def solution(queries, diff):
    num_cnt_dict = {}
    result = []
    curr_result = 0
    for query in queries:
        num = int(query[1:])
        pairs_cnt = num_cnt_dict.get(num + diff, 0) + num_cnt_dict.get(num - diff, 0)
        if diff == 0:
            pairs_cnt = num_cnt_dict.get(num + diff, 0)

        if query[0] == '+':
            curr_result += pairs_cnt
            num_cnt_dict[num] = num_cnt_dict.get(num, 0) + 1
        else:
            curr_result -= pairs_cnt
            num_cnt_dict[num] = num_cnt_dict.get(num, 0) - 1

        result.append(curr_result)

    return result


print(solution(["+4", "+5", "+2", "-4"], 1))  # [0, 1, 1, 0]
print(solution(["+2", "+2", "+4", "+3", "-2"], 1))  # [0, 0, 0, 3, 2]
print(solution(["+2", "+3", "+3", "+2", "-3", "-2", "+2", "+3"], 1))  # [0, 1, 2, 4, 2, 1, 2, 4]
