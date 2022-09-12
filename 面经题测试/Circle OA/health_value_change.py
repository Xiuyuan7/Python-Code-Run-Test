class Solution:
    def health_value_change(self, initial_hp, deltas):
        for delta in deltas:
            initial_hp += delta
            if initial_hp < 0:
                initial_hp = 0
            elif initial_hp > 100:
                initial_hp = 100

        return initial_hp


s = Solution()
initial_hp = 12
deltas = [-4, -12, 6, 2]
print(s.health_value_change(initial_hp, deltas))
