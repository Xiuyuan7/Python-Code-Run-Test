class Solution:
    """
    @params: strs:List[str], m:int
    @return: str
    @Time: O(KN)
    @Space: O(1)
    """
    def odd_strings(self, strs, m):
        str_odd_count = 0

        for s in strs:
            char_even_count = 0

            for char in s:
                if ord(char) % 2 == 0:
                    char_even_count += 1

            if char_even_count == 0:
                str_odd_count += 1

        return 'Even' if str_odd_count % 2 == 0 else 'Odd'


s = Solution()

strs = ['a', 'a']
m = 2
print(s.odd_strings(strs, m))  # Even

strs = ['a', 'b']
m = 2
print(s.odd_strings(strs, m))  # Odd
