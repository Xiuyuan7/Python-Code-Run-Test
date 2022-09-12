class Solution:
    """
    @params: red:List[int], blue:List[int], blueCost:int
    @return: List[int]
    """
    def visiting_cities(self, red, blue, blueCost):
        city_quantity = len(red) + 1
        result = [0]
        # The red_cost_dp list records the minimum cost of arriving current city through the red line from last city
        red_cost_dp = [0] * city_quantity
        # The blue_cost_dp list records the minimum cost of arriving current city through the blue line from last city
        blue_cost_dp = [0] * city_quantity

        # Initialization
        blue_cost_dp[0] = blueCost

        for i in range(1, city_quantity):
            # The minimum cost of red line is the smaller cost of last red line and last blue line, plus current cost
            red_cost_dp[i] = min(red_cost_dp[i - 1], blue_cost_dp[i - 1]) + red[i - 1]
            # The minimum cost of blue line is the smaller cost of last red line + blueCost and last blue line, plus
            # current cost
            blue_cost_dp[i] = min(red_cost_dp[i - 1] + blueCost, blue_cost_dp[i - 1]) + blue[i - 1]
            # The current minimum cost is the smaller cost between from the red line and from the blue line
            result.append(min(red_cost_dp[i], blue_cost_dp[i]))

        return result


s = Solution()

red = [2, 3, 4]
blue = [3, 1, 1]
blueCost = 2

print(s.visiting_cities(red, blue, blueCost))  # [0, 2, 5, 6]
