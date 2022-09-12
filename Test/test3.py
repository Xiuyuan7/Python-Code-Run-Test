def getTotalEfficiency(skill):
    result = 0
    visited = {num: 0 for num in skill}
    teams = len(skill) // 2
    total_skill = sum(skill)
    team_skill = total_skill // teams

    if team_skill * teams != total_skill:
        return -1

    for num1 in skill:
        num2 = team_skill - num1
        if visited[num2] == 0:
            visited[num1] += 1
        else:
            result += num1 * num2
            visited[num2] -= 1

    for value in visited.values():
        if value != 0:
            return -1

    return result


skill = [1, 2, 3, 2]
print(getTotalEfficiency(skill))

skill = [5, 4, 2, 1]
print(getTotalEfficiency(skill))

skill = [2, 1, 1, 4, 3, 5]
print(getTotalEfficiency(skill))

skill = [2, 1, 1, 4, 3, 4]
print(getTotalEfficiency(skill))
