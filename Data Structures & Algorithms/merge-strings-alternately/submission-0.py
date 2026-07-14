class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_string = ''
        shorter_string_len = min(len(word1), len(word2))
        for i in range(shorter_string_len):
            final_string += word1[i] + word2[i]
        if len(word1) > shorter_string_len:
            final_string += word1[shorter_string_len:]
        elif len(word2) > shorter_string_len:
            final_string += word2[shorter_string_len:]
        return final_string
        