class Solution:
    def transforming_strings(self, string):
        # Use a stack to check adjacent characters
        stack = []

        for char in string:
            # Append current character to the stack if the stack is empty
            if not stack:
                stack.append(char)
                continue

            # Pop the top character if adjacent pair exists
            if char == "A" and stack[-1] == "B" or char == "B" and stack[-1] == "A" \
                    or char == "X" and stack[-1] == "Y" or char == "Y" and stack[-1] == "X":
                stack.pop()
            # Otherwise, append current character
            else:
                stack.append(char)

        return "".join(stack)


s = Solution()

string = "ABBA"
print(s.transforming_strings(string))

string = "XYZ"
print(s.transforming_strings(string))
