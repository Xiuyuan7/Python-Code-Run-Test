class Solution:
    def split_message(self, text, limit):
        num_of_chars = len(text)
        digits = 1
        suf_chars = 5
        while True:
            if suf_chars >= limit:
                return []
