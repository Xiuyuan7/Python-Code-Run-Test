class Solution:
    def league_competition(self, wins, draws, scored, conceded):
        winner = 0

        for i in range(1, len(wins)):
            previous_team_points = wins[i - 1] * 3 + draws[i - 1]
            current_team_points = wins[i] * 3 + draws[i]
            if current_team_points > previous_team_points:
                winner = i
            elif current_team_points == previous_team_points:
                previous_net_goals = scored[i - 1] - conceded[i - 1]
                current_net_goals = scored[i] - conceded[i]
                if current_net_goals > previous_net_goals:
                    winner = i

        return winner


s = Solution()

wins = [2, 1, 0]
draws = [1, 5, 6]
scored = [20, 15, 10]
conceded = [20, 10, 15]
print(s.league_competition(wins, draws, scored, conceded))

wins = [3, 1, 2, 2]
draws = [1, 5, 4, 4]
scored = [30, 10, 20, 40]
conceded = [32, 13, 18, 37]
print(s.league_competition(wins, draws, scored, conceded))
