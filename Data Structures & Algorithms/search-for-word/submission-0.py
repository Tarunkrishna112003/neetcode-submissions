class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        def dfs(i: int, j: int, k: int) -> bool:
            # 1. Base Case: Found all letters of the word
            if k == len(word):
                return True
            
            # 2. Out of bounds or character mismatch
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # 3. Mark current cell as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # 4. Explore 4 directions (Up, Down, Left, Right)
            found = (dfs(i - 1, j, k + 1) or
                     dfs(i + 1, j, k + 1) or
                     dfs(i, j - 1, k + 1) or
                     dfs(i, j + 1, k + 1))
            
            # 5. Backtrack: Restore original character
            board[i][j] = temp
            
            return found

        # Try starting DFS from every matching starting cell
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False