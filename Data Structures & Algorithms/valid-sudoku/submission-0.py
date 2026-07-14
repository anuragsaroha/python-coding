class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_sets = [set() for _ in range(len(board))]
        c_sets = [set() for _ in range(len(board[0]))]
        g_sets = [[set() for _ in range(len(board)//3)] for _ in range(len(board[0])//3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                elem = board[r][c]
                if elem == '.':
                    continue
                if elem in r_sets[r] or elem in c_sets[c] or elem in g_sets[r//3][c//3]:
                    return False
                r_sets[r].add(elem)
                c_sets[c].add(elem)
                g_sets[r//3][c//3].add(elem)
        return True
   
        