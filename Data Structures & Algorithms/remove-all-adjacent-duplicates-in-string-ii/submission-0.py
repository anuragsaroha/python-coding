class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s_stack = []
        # repeats = 0
        s_list = list(s)
        for idx, char in enumerate(s_list):
            if s_stack and s_stack[-1][0] == char:
                repeats = s_stack[-1][1] + 1
                s_stack.append([char, repeats])
            else:
                repeats = 1
                s_stack.append([char, repeats])
            if s_stack[-1][1] == k:
                for _ in range(k):
                    s_stack.pop()

        new_s_list = [c[0] for c in s_stack]
        return ''.join(new_s_list)
